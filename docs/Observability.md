# Event-Driven Observability Architecture

## Executive Summary

The Event-Driven Observability Architecture unifies logging, tracing, and metrics collection through a context-based event pipeline. This design provides explicit dependency injection for testability while offering a shared context singleton for convenience. The architecture distinguishes between system observability (infrastructure concerns) and domain observability (business logic), maintaining zero-overhead characteristics when instrumentation is disabled.

## Mental Model

Observability flows through your application as structured events emitted from explicit contexts:

```
Application Boundary
    ↓ 
ObservabilityContext ←── SharedContext (singleton)
    ↓ emit()              ↑ thread-safe access
Domain Objects ──────────→ Events
    ↓
Handler Tree
    ├─→ Sink (I/O operations)
    ├─→ Control (filtering/sampling)
    └─→ Composite (coordination)
```

The architecture provides two access patterns:
- **Explicit Contexts**: Direct instantiation for testing and isolation
- **Shared Context**: Singleton pattern for convenient ambient access

## Architectural Overview

The system implements a four-layer event processing pipeline:

1. **Context Layer**: Encapsulates mutable state and configuration
2. **Event System**: Routes structured events with zero allocation
3. **Domain Layer**: Translates domain operations into events
4. **Handler Layer**: Processes events through composable trees

```
┌─────────────────────────────────────────────────┐
│              Application Code                   │
├─────────────────────────────────────────────────┤
│ ObservabilityContext │ SharedContext.get()      │ ← Context Layer
├─────────────────────────────────────────────────┤
│  Logger │ Span │ Counter (Domain Objects)       │ ← Domain Layer
├─────────────────────────────────────────────────┤
│         EventDict (type, value, metadata)       │ ← Event System
├─────────────────────────────────────────────────┤
│    Handler Tree (Sink/Control/Composite)        │ ← Handler Layer
└─────────────────────────────────────────────────┘
```

## Context Layer

### ObservabilityContext

The primary abstraction encapsulating all observability state:

```python
class ObservabilityContext:
    def __init__(self, config: Optional[ObservabilityConfig] = None):
        self._handlers: List[EventHandler] = []
        self._start_time_ns = time.perf_counter_ns()
        self._lock = threading.Lock()
    
    def emit(self, event_type: str, value: Any, **metadata) -> None:
        """Zero-overhead emission when no handlers attached."""
        if not self._handlers:  # Single boolean check
            return
        # Event construction and dispatch
```

### SharedContext Pattern

A thread-safe singleton providing ambient observability access:

```python
class SharedContext:
    _ctx: Optional[ObservabilityContext] = None
    _lock: threading.Lock = threading.Lock()
    
    @classmethod
    def setup(cls, config: Optional[ObservabilityConfig] = None):
        """Initialize shared context once at application boundary."""
        with cls._lock:
            if cls._ctx is not None:
                raise RuntimeError("Already initialized")
            cls._ctx = ObservabilityContext(config)
    
    @classmethod
    def get(cls) -> ObservabilityContext:
        """Retrieve shared context for ambient access."""
        if cls._ctx is None:
            raise RuntimeError("Not initialized")
        return cls._ctx
```

### Configuration

Immutable configuration loaded at application boundaries:

```python
@dataclass(frozen=True)
class ObservabilityConfig:
    handlers: List[EventHandler] = field(default_factory=list)
    sampling_rate: float = 1.0
    enabled_categories: Set[str] = field(default_factory=set)
```

## Event System

### EventDict Structure

Events flow as structured dictionaries with layered fields:

```python
EventDict = Dict[str, Any]
# Core fields: type, value, timestamp_ns, context_name
# Context fields: trace_id, request_id, operation_id
# Domain fields: logger_name, span_id, metric_labels
# User metadata: arbitrary kwargs
```

### Context Variables

Ambient context enrichment via Python's contextvars:

```python
# Exported directly from observability package
trace_id = contextvars.ContextVar("trace_id", default=None)
request_id = contextvars.ContextVar("request_id", default=None)
operation_id = contextvars.ContextVar("operation_id", default=None)
```

### Performance Characteristics

| State | Overhead | Operation |
|-------|----------|-----------|
| No handlers | <1ns | Single boolean check |
| With handlers | ~100ns | Event construction + dispatch |
| Context lookup | ~20ns | Cached contextvar access |

## Domain Layer

Domains provide specialized APIs that emit structured events:

### Direct Instantiation

```python
from observability.domains.logging import Logger
from observability.domains.tracing import Span
from observability.domains.metrics import Counter

# Create domain objects directly
logger = Logger('myapp.service', context)
span = Span('operation', context)
counter = Counter('requests', context)
```

### Event Type Constants

Pre-computed constants eliminate runtime string construction:

```python
# logging.py
LOG_40: Final[str] = "log.40"  # ERROR level
LOG_20: Final[str] = "log.20"  # INFO level

# tracing.py  
SPAN_START: Final[str] = "span.start"
SPAN_END: Final[str] = "span.end"
```

## Handler Layer

### Handler Types

**Sink Handlers** - Terminal I/O operations:
- `PrintHandler`: Formatted console output
- `JsonHandler`: JSON serialization
- `ManagedFileHandler`: File writing with rotation

**Control Handlers** - Flow modification:
- `filtered()`: Predicate-based filtering
- `sampled()`: Probabilistic sampling
- `AsyncHandlerWorker`: Async queue processing

**Composite Handlers** - Multi-handler coordination:
- `FanoutHandler`: Broadcast to multiple handlers
- `FallbackHandler`: Failover between handlers

### Handler Composition

Direct class instantiation for explicit configuration:

```python
# Development setup
dev_handlers = [
    PrintHandler(sys.stderr),
    ManagedFileHandler('debug.log')
]

# Production setup  
prod_handlers = [
    filtered(
        lambda e: e.get('level', 0) >= ERROR,
        JsonHandler(sys.stderr)
    ),
    sampled(0.01, AsyncHandlerWorker(
        BufferHandler(size=1000)
    ))
]

config = ObservabilityConfig(handlers=prod_handlers)
```

## Usage Patterns

### System Observability (Shared Context)

For infrastructure concerns using ambient access:

```python
# infrastructure/cache.py
from observability.shared import SharedContext
from observability.domains.logging import Logger

# Module-level logger via shared context
logger = Logger(__name__, SharedContext.get())

def get_from_cache(key: str) -> Optional[Any]:
    logger.debug("Cache lookup", key=key)
    # Implementation
```

### Domain Observability (Explicit Context)

For business logic requiring isolation:

```python
# domain/payment_processor.py
from observability.domains.logging import Logger
from observability.domains.metrics import Counter

class PaymentProcessor:
    def __init__(self, gateway: Gateway, obs: ObservabilityContext):
        self.gateway = gateway
        self.logger = Logger('audit.payments', obs)
        self.counter = Counter('payments.total', obs)
    
    def process_payment(self, payment: Payment) -> Result:
        self.logger.info('Payment initiated', 
                        amount=payment.amount,
                        user_id=payment.user_id)
        
        result = self.gateway.charge(payment)
        self.counter.increment(
            status='success' if result.ok else 'failure'
        )
        return result
```

### Testing Patterns

Explicit contexts enable perfect isolation:

```python
def test_payment_logs_amount():
    # Isolated test context
    buffer = BufferHandler()
    config = ObservabilityConfig(handlers=[buffer])
    test_context = ObservabilityContext(config)
    test_context.start()
    
    # Inject test context
    processor = PaymentProcessor(MockGateway(), test_context)
    processor.process_payment(Payment(amount=100.0))
    
    # Verify events
    events = buffer.get_events()
    assert events[0]['amount'] == 100.0
```

## Initialization Patterns

### Application Entry Point

```python
# main.py
from observability import ObservabilityConfig, SharedContext
from observability.handlers import JsonHandler

def main():
    # Initialize shared context once
    config = ObservabilityConfig(
        handlers=[JsonHandler(sys.stderr)],
        sampling_rate=0.1
    )
    SharedContext.setup(config)
    
    # Application runs with ambient access
    run_application()
```

### Library Pattern

```python
# Libraries accept optional contexts
class DataProcessor:
    def __init__(self, obs: Optional[ObservabilityContext] = None):
        # Use provided context or shared
        self.context = obs or SharedContext.get()
        self.logger = Logger('processor', self.context)
```

## Implementation Strategy

### Phase 1: Shared Context
```python
# Initialize at entry point
SharedContext.setup(config)

# Use throughout via SharedContext.get()
logger = Logger('myapp', SharedContext.get())
```

### Phase 2: Explicit Contexts
```python
# Create isolated contexts where needed
special_context = ObservabilityContext(special_config)
special_context.start()

# Pass explicitly for isolation
service = Service(special_context)
```

### Phase 3: Full Adoption
```python
# Shared for system concerns
system_logger = Logger(__name__, SharedContext.get())

# Explicit for domain logic
class BusinessService:
    def __init__(self, obs: ObservabilityContext):
        self.metrics = Counter('business', obs)
```

## Conclusion

The Event-Driven Observability Architecture provides a foundation balancing explicit dependency management with practical convenience. The SharedContext singleton acknowledges the reality of ambient logging needs while maintaining the option for explicit context injection where isolation matters. The direct instantiation approach keeps the API surface minimal while enabling sophisticated handler composition through simple class construction.