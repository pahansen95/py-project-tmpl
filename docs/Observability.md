# Event-Driven Observability Architecture

## Executive Summary

The Event-Driven Observability Architecture unifies logging, tracing, and metrics collection through a context-based event pipeline. This design provides both explicit dependency injection for testability and convenient ambient access for common cases. The architecture distinguishes between system observability (infrastructure concerns) and domain observability (business logic), allowing appropriate patterns for each while maintaining zero-overhead characteristics.

## Mental Model

Observability is a **capability** that flows through your application via explicit contexts, with convenient defaults for common cases:

```
Application Boundary
    ↓ initialize
ObservabilityContext ──→ Default Context (optional)
    ↓ pass/inject          ↓ ambient access
Domain Objects          System Modules
    ↓ emit                 ↓ emit
Event Pipeline
    ↓ dispatch
Handler Tree
```

The architecture supports two complementary patterns:
- **Explicit Contexts**: For domain logic, testing, and isolation
- **Ambient Defaults**: For system observability and convenience

## Architectural Overview

The architecture consists of four primary layers:

1. **Context Layer**: Manages observability state and configuration
2. **Core Event System**: Routes events from producers to consumers
3. **Domain API Layer**: Provides specialized interfaces for different concerns
4. **Handler Pipeline**: Processes events for output and analysis

```
┌─────────────────────────────────────────────────┐
│              Application Code                   │
├─────────────────────────────────────────────────┤
│   Explicit Context  │  Default Context          │ ← Context Layer
├─────────────────────────────────────────────────┤
│  Logging │ Tracing │ Metrics (Domain APIs)     │ ← Domain Layer
├─────────────────────────────────────────────────┤
│            Core Event System                    │ ← Event Router
├─────────────────────────────────────────────────┤
│         Handler Pipeline & Processing           │ ← Event Consumers
└─────────────────────────────────────────────────┘
```

## Context Layer

The context layer provides explicit state management with convenient defaults.

### ObservabilityContext

The primary abstraction that encapsulates all mutable state:

```python
class ObservabilityContext:
    """Explicit context for observability state."""
    
    def __init__(self, config: ObservabilityConfig):
        self._handlers: List[Handler] = []
        self._start_time = time.perf_counter_ns()
        self._config = config
    
    def emit(self, event_type: str, value: Any, **metadata) -> None:
        """Emit event with zero overhead when no handlers attached."""
        if not self._handlers:  # Single check optimization
            return
        # Event processing...
```

### Configuration Management

Configuration flows from application boundaries inward:

```python
@dataclass
class ObservabilityConfig:
    """Immutable configuration loaded at boundaries."""
    handlers: List[HandlerConfig]
    sampling_rate: float = 1.0
    enable_categories: Set[str] = field(default_factory=set)
    
# At application startup
config = ObservabilityConfig(
    handlers=[FileHandlerConfig('app.log')],
    sampling_rate=0.01
)
obs_context = create_observability(config)
```

### Default Context Pattern

For convenience, a default context provides ambient access:

```python
# Initialize once at application boundary
observability.initialize_default(config)

# Use anywhere via convenience functions
from observability import emit
emit('user.action', action='login')

# Or explicitly override
special_context = create_observability(special_config)
process_sensitive_data(data, obs=special_context)
```

## Usage Patterns

### System Observability (Module-Level)

Appropriate for infrastructure concerns, debugging, and operational metrics:

```python
# infrastructure/cache.py
from observability import get_default

# Module-level logger for system observability
logger = get_default().create_logger(__name__)

def get_from_cache(key: str) -> Optional[Any]:
    logger.debug(f"Cache lookup: {key}")
    # Implementation...
```

**When to use**:
- Debug logging
- Performance metrics
- Error tracking
- System health monitoring

### Domain Observability (Dependency Injection)

Required for business logic, audit trails, and testable components:

```python
# domain/payment_processor.py
class PaymentProcessor:
    def __init__(self, gateway: Gateway, obs: ObservabilityContext):
        self.gateway = gateway
        self.audit_log = obs.create_logger('audit.payments')
        self.metrics = obs.create_metrics('payments')
    
    def process_payment(self, payment: Payment) -> Result:
        self.audit_log.info('payment.initiated', 
                          amount=payment.amount,
                          user_id=payment.user_id)
        
        with self.metrics.timer('processing_time'):
            result = self.gateway.charge(payment)
            
        self.metrics.counter('total').increment(
            status='success' if result.ok else 'failure'
        )
        return result
```

**When to use**:
- Business metrics
- Audit logging
- Compliance tracking
- Component isolation for testing

### Testing Patterns

Explicit contexts enable perfect test isolation:

```python
def test_payment_processor_logs_amount():
    # Create isolated test context
    buffer = BufferHandler()
    test_config = ObservabilityConfig(handlers=[buffer])
    test_context = create_observability(test_config)
    
    # Inject test context
    processor = PaymentProcessor(MockGateway(), test_context)
    processor.process_payment(Payment(amount=100.0))
    
    # Verify events
    events = buffer.get_events()
    assert events[0]['amount'] == 100.0
```

## Core Event System

The event system is a lightweight publish-subscribe mechanism accessed through contexts.

### Event Model

Events are structured records containing:
- **Type**: Hierarchical identifier (e.g., 'log.error', 'metric.counter')
- **Value**: Primary payload
- **Timestamp**: High-precision timing relative to context creation
- **Context**: Automatic capture from contextvars
- **Metadata**: Additional key-value pairs

### Performance Characteristics

Zero-overhead design through context-based optimization:

| State | Overhead | Operation |
|-------|----------|-----------|
| No handlers | <1ns | Single boolean check |
| With handlers | ~100ns | Event construction + dispatch |
| Context lookup | ~20ns | Cached contextvar access |

### Context Propagation

Ambient context enriches events automatically:

```python
import contextvars

trace_id = contextvars.ContextVar('trace_id')
request_id = contextvars.ContextVar('request_id')

# Set at request boundary
request_id.set('req-123')

# Automatically included in all events
obs_context.emit('user.action', action='login')
# Event includes: {'request_id': 'req-123', ...}
```

## Domain APIs

Domain-specific APIs provide intuitive interfaces while emitting structured events.

### Logging Domain
```python
logger = obs_context.create_logger('myapp')
logger.info('User logged in', user_id=123)
# Emits: {'type': 'log.info', 'message': 'User logged in', 'user_id': 123}
```

### Metrics Domain
```python
metrics = obs_context.create_metrics('api')
metrics.counter('requests').increment(endpoint='/users')
# Emits: {'type': 'metric.counter', 'name': 'api.requests', 'value': 1, 'endpoint': '/users'}
```

### Tracing Domain
```python
tracer = obs_context.create_tracer('service')
with tracer.span('database.query') as span:
    span.set_tag('query_type', 'SELECT')
# Emits: {'type': 'span.start', ...} and {'type': 'span.end', ...}
```

## Handler Pipeline

Handlers process events without blocking emission, maintaining isolation between different processing strategies.

### Handler Composition

```python
# Development configuration
dev_handler = fanout(
    create_console_handler(color=True),
    create_file_handler('debug.log', level=DEBUG)
)

# Production configuration
prod_handler = fanout(
    filtered(lambda e: e.get('level') >= ERROR, 
             create_alert_handler()),
    sampled(0.01, async_handler(
        create_metrics_handler()
    )),
    async_handler(create_file_handler('app.log'))
)
```

## Initialization Patterns

### Simple Application

```python
# main.py
from observability import initialize_default

def main():
    # Initialize default context at entry point
    initialize_default(ObservabilityConfig(
        handlers=[create_console_handler()]
    ))
    
    # Rest of application uses simple API
    run_application()
```

### Complex Application

```python
# app.py
def create_app(config: AppConfig) -> Application:
    # Create explicit context
    obs_config = ObservabilityConfig(
        handlers=[
            create_file_handler(config.log_file),
            create_metrics_handler(config.metrics_endpoint)
        ],
        sampling_rate=config.sampling_rate
    )
    obs_context = create_observability(obs_config)
    
    # Wire through application
    return Application(
        database=Database(config.db_url, obs_context),
        api=APIServer(obs_context),
        obs_context=obs_context
    )
```

### Library Pattern

```python
# For libraries that need observability
class DataProcessor:
    def __init__(self, obs: Optional[ObservabilityContext] = None):
        self.obs = obs or null_context()  # Null object pattern
        self.logger = self.obs.create_logger('processor')
    
    def process(self, data: Data) -> Result:
        self.logger.debug('Processing started', size=len(data))
        # ...
```

## Implementation Strategy

The architecture supports gradual adoption across large codebases:

### Phase 1: Default Context
```python
# Add default context initialization
observability.initialize_default(config)

# Simple emit() calls work via default
emit('event', value=42)
```

### Phase 2: Explicit Contexts
```python
# Code uses explicit contexts
def new_service(obs: ObservabilityContext):
    obs.emit('service.started')

# Support both patterns
def flexible_function(data, obs=None):
    obs = obs or get_default()
    obs.emit('processing', size=len(data))
```

### Phase 3: Full Adoption
```python
# All code uses explicit contexts
# Module-level for system observability
logger = get_default().create_logger(__name__)

# DI for domain observability
class BusinessService:
    def __init__(self, obs: ObservabilityContext):
        self.metrics = obs.create_metrics('business')
```

## Benefits and Trade-offs

### Benefits

**Explicit Dependencies**:
- Clear in function signatures
- Perfect test isolation
- Multiple configurations possible
- No hidden global state

**Flexible Patterns**:
- Ambient access for convenience
- Explicit injection for testing
- Module-level for system concerns
- DI for domain logic

**Maintained Performance**:
- Zero-overhead when disabled
- Context enables optimization
- Efficient handler dispatch

### Trade-offs

**Increased Verbosity**:
- Additional parameters in signatures
- Context threading through layers
- More setup code in tests

**Learning Curve**:
- Two patterns to understand
- When to use which approach
- Implementation complexity

## Conclusion

The Event-Driven Observability Architecture provides a sophisticated foundation that balances explicit dependency management with developer convenience. By supporting both ambient and injected patterns, it acknowledges that observability serves different purposes at different layers of the application. The context-based approach ensures testability and flexibility while maintaining the zero-overhead performance characteristics essential for production systems.