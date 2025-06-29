# Python API Specification

## About This Document

This reference establishes standards for Python API Specifications - the contractual interface definitions between library maintainers and users.

### Mental Model

API Specifications serve three interconnected purposes:

1. **Contractual Boundary**: Defines the stable interface with versioning guarantees
2. **Prescriptive Guide**: Directs users toward successful integration patterns  
3. **Self-Contained Reference**: Provides complete understanding without external documentation

The specification is not merely documentation of what exists, but a deliberate design of what users should interact with. In Python's open ecosystem where all code is technically accessible, the API Specification carves out the supported interaction surface.

### Design Philosophy

- **Explicit over Discovered**: Exported names are explicitly chosen, not automatically derived
- **Prescriptive over Descriptive**: Guides correct usage rather than documenting all possibilities
- **Hierarchical Disclosure**: Progressive layers from highly prescribed to loosely guided
- **Examples as Contract**: Usage examples demonstrate both how and what is guaranteed

### Relationship to Implementation

API Specifications document the designed interface, not the implementation structure. Public modules may exist without specifications if users should not import from them directly. The presence of a specification file is itself a design decision endorsing that import path.

## 1. Introduction

### 1.1 Purpose

This document defines normative requirements for Python API Specifications - the authoritative contract between library maintainers and users. An API Specification establishes the supported interface boundary, prescribes correct usage patterns, and provides self-contained reference documentation that supersedes external documentation for contractual purposes.

### 1.2 Scope

This specification applies to Python libraries intended for public distribution. It covers:
- Stub file placement based on import patterns
- Documentation requirements for exported names
- Type annotation standards
- Export policies and versioning guarantees

Key principle: API specifications are prescriptive design documents that define how users should interact with a library, not comprehensive catalogs of available functionality.

### 1.3 Conventions

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in RFC 2119.

### 1.4 Terminology

- **API Specification**: A Python stub file (`.pyi`) documenting exported names
- **Export**: To include a name in a formal API specification, granting major version stability
- **Private Name**: An identifier prefixed with underscore, no stability guarantees
- **Public Name**: An identifier not prefixed with underscore, stable within minor versions
- **Exported Name**: A public name included in an API specification, stable within major versions
- **Import Point**: A module or package from which users are intended to import
- **Internal Module**: Implementation module not intended for direct import (may be private or public)

## 2. File Organization

### 2.1 Stub File Placement

API specifications document EXPORTED names at their intended import locations. The presence of a stub file is an explicit endorsement of that import path. Absence of a stub, even for public modules, signals "not part of the designed interface."

```
# Package with unified API (single import point)
src/
└── library/
    ├── __init__.py       # Exports: Process, Config, run()
    ├── __init__.pyi      # Single API spec for all exports
    ├── process.py        # Public module - but no stub needed
    ├── config.py         # Public module - but no stub needed
    ├── utils.py          # Public module - but no stub needed
    └── _internal.py      # Private module

# In this case:
# - process.py, config.py, utils.py are PUBLIC (no underscore)
# - But they don't get stubs because users should import from library
# - Only library/__init__.pyi documents the EXPORTED API

# Namespace package (no __init__.py) - independent modules
src/
└── converters/           # Namespace package - no __init__.py
    ├── json2xml.py       # Users import: from converters.json2xml import convert
    ├── json2xml.pyi      # API spec for json2xml module
    ├── xml2csv.py        # Users import: from converters.xml2csv import convert  
    ├── xml2csv.pyi       # API spec for xml2csv module
    ├── yaml2json.py      # Users import: from converters.yaml2json import convert
    └── yaml2json.pyi     # API spec for yaml2json module

# In namespace packages:
# - Each module is completely independent
# - Each module is its own import point
# - Each module gets its own stub
# - No __init__.pyi because there's no __init__.py
```

### 2.2 File Naming Requirements

- Package specifications MUST use `__init__.pyi` when the package exports names
- Module specifications MUST match the module name: `module.pyi` 
- Only modules at intended import points SHOULD have specifications
- Public modules re-exported by packages MUST NOT have separate specifications

Example:
```python
# library/__init__.py re-exports from public modules
from .connection import Connection
from .client import Client
from .errors import NetworkError

# Only library/__init__.pyi needed:
class Connection: ...
class Client: ...  
class NetworkError(Exception): ...

# No stubs for connection.py, client.py, errors.py even though they're public
# Users should import: from library import Connection
# Not: from library.connection import Connection
```

### 2.3 Import-Based Structure

API specifications MUST reflect the intended import patterns, not implementation structure:

- If users import from a package (`from pkg import Class`), only `pkg/__init__.pyi` is needed
- If users import from a module (`from pkg.module import func`), then `pkg/module.pyi` is needed
- Internal modules that are re-exported through `__init__.py` do NOT need separate stubs

### 2.4 Export Principles

API specifications document the EXPORTED public names at their intended import points. Stub files establish the boundary between supported API (exported) and available implementation (public). This boundary is a design decision, not a mechanical derivation.

Example - Three-Tier Distinction:
```
# Library structure
library/
├── __init__.py       # from .engine import Engine
├── __init__.pyi      # class Engine: ...  (EXPORTED)
├── engine.py         # PUBLIC module with Engine class
├── utils.py          # PUBLIC module with helper functions
└── _internal.py      # PRIVATE module

# Tier 1: Exported API (documented in stubs)
from library import Engine  # ✓ Stable, recommended

# Tier 2: Public but not exported (no stubs)
from library.engine import Engine  # Works but not guaranteed
from library.utils import helper   # Public but no major version guarantee

# Tier 3: Private usage
from library._internal import State  # No guarantees at all
```

## 3. Specification Structure

### 3.1 Recommended API Specification Structure

For consistency across projects, API specifications SHOULD follow this five-section template. While simpler APIs may use abbreviated structures, this template provides a comprehensive framework suitable for most libraries:

#### Template Structure

1. **API Spec Overview** - Module docstring with purpose, examples, and mental model
2. **Python & External Imports** - All necessary imports
3. **API Type Aliases, Protocols, Enums** - Type definitions
4. **API Core Types & Functionality** - Primary exported interface
5. **API Supporting Types & Functionality** - Secondary utilities

This structure may be adapted based on API complexity:
- **Minimal APIs**: May combine or omit sections
- **Complex APIs**: Should use the full structure with detailed subsections

#### 3.1.1 API Spec Overview
The module docstring providing comprehensive API documentation:

```python
"""Single-line summary of the API purpose.

Extended description containing:
- What functionality the API provides
- Expected behaviors and guarantees
- When and why to use this API
- Key architectural decisions

## Quick Start

Minimal working example:

    from library import MainClass
    instance = MainClass()
    result = instance.process(data)

## Mental Model

Conceptual framework explaining how the API works internally,
why it's structured this way, and how components interact.

## Usage Guidelines

Detailed patterns for common use cases, edge cases, and 
best practices for integrating the API.
"""
```

#### 3.1.2 Python & External Imports
All import statements, starting with future imports:

```python
from __future__ import annotations  # REQUIRED first line
from typing import Protocol, TypeAlias, Any, Optional
import external_dependency
from external_package import ExternalType
```

#### 3.1.3 API Type Aliases, Protocols, Enums
Type definitions ordered by complexity:

```python
# Type aliases with brief docstrings
ConfigDict: TypeAlias = dict[str, Any]
"""Configuration mapping for initialization."""

# Enums with purpose documentation
class Status(Enum):
    """Processing status states."""
    PENDING = "pending"
    ACTIVE = "active"
    COMPLETE = "complete"

# Protocols with comprehensive contracts
class ProcessorProtocol(Protocol):
    """
    Contract for data processors.
    
    Defines the interface that all processors must implement,
    including both synchronous and asynchronous variants.
    """
    def process(self, data: bytes) -> Result: ...
```

#### 3.1.4 API Core Types & Functionality
Primary exported functionality that users directly interact with. Comprehensive documentation required.

#### 3.1.5 API Supporting Types & Functionality
Secondary functionality that supports the core API. Documentation explains relationship to core functionality.

### 3.2 Section Formatting Requirements

#### 3.2.1 Section Separators
Each major section MUST be visually separated with comment blocks:

```python
# ruff: noqa: F811
"""API Spec Overview..."""

from __future__ import annotations
# ... other imports ...

# =============================================================================
# API Type Aliases, Protocols, Enums
# =============================================================================

# ... type definitions ...

# =============================================================================
# API Core Types & Functionality
# =============================================================================

# ... core API ...

# =============================================================================
# API Supporting Types & Functionality
# =============================================================================

# ... supporting API ...
```

#### 3.2.2 Ordering Within Sections

**Type Definitions Section** - Order by dependency and complexity:
1. Simple type aliases
2. Enums
3. Complex type aliases (using other types)
4. Protocols (simplest to most complex)

**Core API Section** - Order by importance and usage frequency:
1. Primary classes/functions users interact with most
2. Essential data structures
3. Main processing functions
4. Configuration classes

**Supporting API Section** - Order by relationship to core:
1. Factory functions for core types
2. Utility functions
3. Helper classes
4. Advanced/specialized functionality

### 3.3 Documentation Standards Per Section

#### 3.3.1 Documentation Depth Guidelines

Documentation depth should match complexity and user needs:

**Minimal Documentation**
- Properties, simple methods, obvious operations
- Single-line purpose statement
- Constraints noted inline (read-only, ranges)

```python
@property
def name(self) -> str:
    """Entity name (read-only)."""
    ...
```

**Standard Documentation**  
- Core classes, primary functions
- Purpose, parameters, return values
- Single clarifying example
- Key behavioral notes

```python
def process(data: bytes) -> str:
    """
    Convert raw bytes to normalized string.
    
    Args:
        data: UTF-8 encoded bytes
        
    Returns:
        Normalized string with whitespace trimmed
        
    Example:
        result = process(b'  hello  ')
        assert result == 'hello'
    """
    ...
```

**Comprehensive Documentation**
- Complex patterns, framework entry points
- Full behavioral specification
- Multiple usage examples  
- Integration patterns
- Performance characteristics

#### 3.3.2 Import Section Requirements

```python
# ALWAYS first (required for all stubs)
from __future__ import annotations

# Standard library types needed for annotations
from typing import Protocol, TypeAlias, Optional, Union, Any
from collections.abc import Sequence, Mapping

# External dependencies (if any)
import numpy as np
from external_lib import RequiredType

# No relative imports in stubs - use full package paths
from mypackage.types import SharedType  # Not: from .types import
```

#### 3.3.3 Type Definition Documentation

**Type Aliases** - Brief single-line docstrings:
```python
ConfigDict: TypeAlias = dict[str, Any]
"""Runtime configuration parameters."""

FilterFunc: TypeAlias = Callable[[Event], bool]
"""Predicate for event filtering."""
```

**Enums** - Purpose and value meanings:
```python
class ProcessingMode(Enum):
    """
    Processing strategy selection.
    
    Determines the execution model and resource allocation.
    """
    SERIAL = "serial"      # Single-threaded execution
    PARALLEL = "parallel"  # Multi-threaded with thread pool
    ASYNC = "async"        # Asynchronous with event loop
```

**Protocols** - Comprehensive contract documentation:
```python
class DataSource(Protocol):
    """
    Contract for data acquisition implementations.
    
    Defines the interface for retrieving data from various sources
    with consistent error handling and retry semantics.
    
    Implementations must:
    - Handle connection failures gracefully
    - Respect timeout constraints
    - Provide meaningful error messages
    - Support cancellation via context
    """
    
    def fetch(self, query: Query) -> Result:
        """Retrieve data matching query parameters."""
        ...
```

#### 3.3.4 Core API Documentation Standards

Every exported name in the Core API section MUST have comprehensive documentation:

**Classes** - Complete behavioral documentation:
```python
class CoreProcessor:
    """
    Single-line purpose statement.
    
    Extended description covering:
    - Primary responsibility and role in the system
    - Behavioral guarantees and constraints  
    - Thread safety and performance characteristics
    - Relationship to other core components
    
    Args:
        config: Configuration dictionary with keys:
            - 'timeout': Maximum seconds per operation (default: 30)
            - 'retry': Number of retry attempts (default: 3)
            - 'mode': Processing mode from ProcessingMode enum
        logger: Optional logger instance for operation tracking
        
    Raises:
        ConfigError: Missing required config keys or invalid values
        RuntimeError: Processor already initialized
        
    Example:
        processor = CoreProcessor({'mode': ProcessingMode.PARALLEL})
        result = processor.execute(data)
        
    Note:
        Instances are thread-safe after initialization.
    """
```

#### 3.3.5 Supporting API Documentation Standards

Supporting functionality MUST explain its relationship to the core API:

```python
def create_default_processor() -> CoreProcessor:
    """
    Factory function creating processor with standard configuration.
    
    Creates a CoreProcessor optimized for general-purpose use.
    
    Returns:
        Configured CoreProcessor ready for use
        
    See Also:
        - CoreProcessor: For custom configuration
        - ProcessorBuilder: For complex configurations
    """
    ...
```

### 3.4 Complete Structure Example

A complete API specification following the recommended structure demonstrates proper organization and documentation depth. See Section 8 for full examples.

## 4. Documentation Standards

### 4.1 Class Documentation

Every exported class MUST include:

```python
class ExportedClass:
    """
    Single-line purpose statement.
    
    Extended description explaining behavior and guarantees.
    
    Args:
        param: Parameter purpose and constraints
        
    Raises:
        ValueError: When and why raised
        
    Example:
        >>> instance = ExportedClass(param=value)
        >>> instance.method()
    """
```

### 4.2 Method Documentation

Public methods MUST document:
- Purpose and behavior
- Parameter semantics (beyond type information)
- Return value meaning
- Side effects
- Exception conditions

### 4.3 Type Alias Documentation

Type aliases MUST include purpose:

```python
ConfigDict: TypeAlias = dict[str, Any]
"""Configuration options for initialization."""
```

### 4.4 Protocol Documentation

Protocols MUST describe the contract:

```python
class HandlerProtocol(Protocol):
    """
    Contract for event handlers.
    
    Implementers must handle events without raising
    exceptions and support optional lifecycle methods.
    """
    def __call__(self, event: Event) -> None: ...
```

### 4.5 Examples as Specification

Examples in API specifications serve as both teaching aids and behavioral contracts:

**Demonstrative Examples**: Show correct usage patterns
**Contractual Examples**: Define guaranteed behaviors

```python
def batch_process(items: list[T]) -> list[Result[T]]:
    """
    Process items preserving order.
    
    Example:
        # Order preservation is guaranteed
        results = batch_process([a, b, c])
        assert results[0].input == a
        assert results[1].input == b
        assert results[2].input == c
    """
```

The example establishes order preservation as a contractual guarantee.

## 5. Export Design Principles

### 5.1 Export Decision Framework

Exports are chosen based on design intent, not mere availability:

**Fundamental Constraint**: API specifications MUST only export names that exist in the implementation. Stubs document the designed subset of existing functionality - they MUST NOT introduce new names, type aliases, or constructs not present in the actual code.

```python
# implementation.py
class Engine: ...
EngineConfig = dict[str, Any]  # Exists in implementation

# implementation.pyi
class Engine: ...              # ✓ Good: Exists in implementation
EngineConfig: TypeAlias = dict[str, Any]  # ✓ Good: Documents existing alias

# WRONG: Adding names that don't exist
EngineOptions: TypeAlias = dict[str, Any]  # ✗ Bad: Not in implementation
```

**Export Criteria** - A name should be exported when it:
1. Forms part of the intended user interface
2. Provides clear value without implementation knowledge
3. Maintains stability within major versions
4. Supports static analysis and IDE discovery

**Non-Export Criteria** - A name should NOT be exported when it:
1. Requires implementation understanding
2. May change frequently
3. Exists primarily for internal use
4. Provides multiple ways to accomplish the same task

### 5.2 Export Categories

**Primary Exports** (Always include)
- Core functionality users directly interact with
- Configuration and initialization patterns  
- Context managers for resource handling
- Type definitions clarifying contracts

**Secondary Exports** (Include when valuable)
- Convenience functions and helpers
- Alternative constructors
- Specialized error types
- Advanced configuration options

**Non-Exports** (Exclude even if public)
- Implementation base classes
- Internal helpers (even without underscore)
- Debugging utilities
- Complex overloads

### 5.3 Naming Hierarchy

Libraries have three levels of names with different guarantees:

```python
# 1. Private Names - No guarantees, can change anytime
_internal_function()  # From any module
library._internal.py  # Private module

# 2. Public Names - Stable within minor versions (1.2.x)
public_function()     # From any module  
library/public.py     # Public module (no underscore)

# 3. Exported Names - Stable within major versions (1.x.x)
exported_function()   # Listed in a .pyi file at intended import point
# These are the PUBLIC names that appear in API specifications
```

Example:
```python
# library/engine.py - PUBLIC module
class Engine: ...         # PUBLIC name
def start_engine(): ...   # PUBLIC name
def _initialize(): ...    # PRIVATE name

# library/__init__.py
from .engine import Engine, start_engine
__all__ = ['Engine']      # Only Engine is EXPORTED

# library/__init__.pyi - API specification
class Engine: ...         # EXPORTED name (in stub)
# start_engine is PUBLIC but not EXPORTED (not in stub)
```

### 5.4 Versioning Guarantees

The three-tier system provides different stability guarantees:

- **Private Names** (underscore prefix): 
  - NO guarantees
  - May change in any release (1.2.3 → 1.2.4)
  - Example: `_helper()`, `library/_internal.py`

- **Public Names** (no underscore, not in stubs):
  - Stable within minor versions
  - Breaking changes require minor version bump (1.2.x → 1.3.0)
  - Example: `library.utils.helper()` when `helper` isn't in any `.pyi`

- **Exported Names** (in API specifications):
  - Stable within major versions
  - Breaking changes require major version bump (1.x.x → 2.0.0)
  - Example: `library.Process` when `Process` is in `library/__init__.pyi`

This creates a clear migration path:
1. Experimental features start as private (`_feature`)
2. Mature to public but not exported (`feature`)
3. Stabilize as exported (in `.pyi` file)

## 6. Type Annotations

### 6.1 Type Completeness

All exported names MUST have complete type annotations:

```python
def process(data: bytes, *, timeout: float = 30.0) -> Result: ...
```

### 6.2 Generic Types

Generic types SHOULD use descriptive type variables:

```python
from typing import TypeVar

T = TypeVar('T')
ConfigT = TypeVar('ConfigT', bound=BaseConfig)
```

### 6.3 Union Types

Prefer `Union` types that reflect actual usage:

```python
# Good: Reflects actual return possibilities
def parse(text: str) -> Union[Document, ParseError]: ...

# Avoid: Too permissive
def parse(text: str) -> Any: ...
```

### 6.4 Type Annotations as Domain Language

Type annotations express computational constraints without introducing new abstractions:

**Constraint Expression**
```python
# Good: Constrains using existing types
Status = Literal['pending', 'active', 'complete']
Port = int  # Document constraints: "Port (0-65535)"

# Avoid: Creating new runtime types
PositiveInt = NewType('PositiveInt', int)  # Don't add
```

**Cognitive Simplification**
```python
# Good: Simplifies complex composition  
JsonDict = dict[str, Union[str, int, float, bool, None, list, dict]]

# Avoid: Needless aliasing
StringType = str  # No cognitive benefit
```

## 7. Progressive Usage Disclosure

### 7.1 Layered API Design

APIs should guide users through progressive complexity layers:

**Layer 1: Primary Interface** (Highly Prescribed)
Core functionality for 90% of use cases. Fully documented in stubs with clear examples.

**Layer 2: Advanced Features** (Moderately Prescribed)  
Power-user features with additional complexity. Documented in stubs but may require more understanding.

**Layer 3: Extension Points** (Loosely Guided)
Public but non-exported APIs for extending functionality. Users accept minor version instability.

**Layer 4: Implementation Details** (Unprescribed)
Private or internal APIs. No guarantees provided.

### 7.2 Layer Documentation

Each layer requires different documentation approaches:

```python
"""
## Usage Patterns

### Standard Usage (Layer 1)
Most users should start here:
    from library import process
    result = process(data)

### Advanced Usage (Layer 2)  
For complex requirements:
    from library import Process
    proc = Process(custom_config)
    result = proc.run(data)

### Extension (Layer 3)
For framework extensions (less stable):
    from library.core import BaseProcessor  # Note: No stub
    class Custom(BaseProcessor): ...
"""
```

### 7.3 Deprecation Management

Managing API evolution through the layers:

```python
import warnings
from typing import deprecated

@deprecated("Use new_function instead")
def old_function() -> None:
    """
    Deprecated: Will be removed in v3.0.
    
    Use new_function() for improved performance.
    """
    warnings.warn(
        "old_function is deprecated, use new_function",
        DeprecationWarning,
        stacklevel=2
    )
    ...
```

Migration strategy:
1. Add deprecation warning in minor release
2. Remove from stub in next major release
3. Move to private name in following major release

## 8. Examples

### 8.1 Complete API Specification

Example of a package with unified API surface:

```python
# library/__init__.pyi
# ruff: noqa: F811
"""Event handling system for asynchronous operations.

Provides a flexible event dispatch mechanism supporting multiple
handlers, filtering, and async execution. Designed for building
reactive applications with loose coupling between components.

## Quick Start

    from events import EventBus, Event
    
    bus = EventBus()
    bus.subscribe('user.login', handle_login)
    bus.publish(Event('user.login', user_id=123))

## Mental Model

Events flow through a pipeline of handlers, each potentially
transforming or reacting to the event. The bus ensures reliable
delivery and error isolation.

## Usage Guidelines

Subscribe handlers to specific event types using dot-notation patterns.
Handler exceptions are logged but don't interrupt event flow.
"""

from __future__ import annotations
from typing import Protocol, TypeAlias, Any, Callable, Optional

# =============================================================================
# API Type Aliases, Protocols, Enums
# =============================================================================

EventType: TypeAlias = str
"""Dot-separated event type identifier."""

EventData: TypeAlias = dict[str, Any]
"""Arbitrary event payload data."""

class EventHandler(Protocol):
    """
    Contract for event handlers.
    
    Handlers process events without raising exceptions.
    Failed handlers should log errors internally.
    """
    def __call__(self, event: Event) -> None: ...

# =============================================================================
# API Core Types & Functionality
# =============================================================================

class Event:
    """
    Immutable event with type and data.
    
    Events represent state changes or signals in the system.
    Once created, events cannot be modified.
    
    Args:
        type: Dot-separated event identifier
        **data: Arbitrary event payload
        
    Example:
        event = Event('user.action', action='click', target='button')
    """
    def __init__(self, type: EventType, **data: Any) -> None: ...
    
    @property
    def type(self) -> EventType:
        """Event type identifier."""
        ...
    
    @property
    def data(self) -> EventData:
        """Event payload data."""
        ...

class EventBus:
    """
    Central event distribution system.
    
    Manages handler registration and event routing with
    support for wildcards and filtering.
    """
    def __init__(self) -> None: ...
    
    def subscribe(self, pattern: str, handler: EventHandler) -> None:
        """Register handler for event pattern."""
        ...
    
    def publish(self, event: Event) -> None:
        """Distribute event to matching handlers."""
        ...

# Note: Implementation may be spread across multiple internal modules
# (_events.py, _bus.py, _handlers.py) but the API surface is unified
```

### 8.2 Multiple Import Points Example

Example of a package with separate module imports:

```python
# library/client.pyi - Users import: from library.client import Client
"""Synchronous client for API access."""

from __future__ import annotations

class Client:
    """Synchronous API client."""
    def __init__(self, url: str) -> None: ...
    def get(self, path: str) -> Response: ...

# library/async_client.pyi - Users import: from library.async_client import AsyncClient  
"""Asynchronous client for API access."""

from __future__ import annotations

class AsyncClient:
    """Asynchronous API client."""
    def __init__(self, url: str) -> None: ...
    async def get(self, path: str) -> Response: ...

# library/__init__.py might be empty or just provide version info
# No library/__init__.pyi needed if it exports nothing
```

### 8.3 Three-Tier Example

Complete example showing private, public, and exported names:

```python
# library/data.py - PUBLIC module (no underscore)
"""Data processing utilities."""

def process(data: bytes) -> str:
    """Process raw data."""  # PUBLIC function
    return _normalize(_parse(data))

def validate(data: str) -> bool:
    """Validate processed data."""  # PUBLIC function
    return len(data) > 0

def _parse(data: bytes) -> str:
    """Internal parsing."""  # PRIVATE function
    return data.decode()

def _normalize(text: str) -> str:
    """Internal normalization."""  # PRIVATE function  
    return text.strip()

# library/__init__.py
from .data import process  # Only importing process
__all__ = ['process']      # Only exporting process

# library/__init__.pyi - API Specification
"""Data processing library with stable API."""

def process(data: bytes) -> str:
    """Process raw data with validation."""
    ...

# Status:
# - process: EXPORTED (in stub) - major version guarantee
# - validate: PUBLIC (no underscore) - minor version guarantee  
# - _parse, _normalize: PRIVATE - no guarantees
# - data.py: PUBLIC module but no stub (not an intended import point)
```

### 8.4 Anti-Patterns

```python
# AVOID: Creating stubs for non-exported public modules
library/
├── __init__.py       # from .data import process
├── __init__.pyi      # def process(): ...
├── data.py           # Public module with multiple functions
└── data.pyi          # WRONG: Not an intended import point

# AVOID: Documenting public but non-exported names in stubs
# library/__init__.pyi
def process(): ...    # Exported
def validate(): ...   # WRONG: Public but not exported (not in __init__.py)

# AVOID: Exposing internal structure
# __init__.pyi  
from ._internal import InternalClass  # Never expose private modules

# AVOID: Creating stubs without clear import intent
library/
└── utils/
    ├── helpers.py    # Public module
    └── helpers.pyi   # Only if users should import from library.utils.helpers
```

### 8.5 Export Curation Example

Implementation contains many names, but exports are curated:

```python
# processor.py - Implementation
class Processor: ...                  # Core class
class ProcessorConfig: ...           # Configuration  
class ProcessorError(Exception): ... # Public error
def create_processor(): ...          # Factory
def validate_config(): ...           # Helper
def _internal_helper(): ...          # Private
class ProcessorBase: ...             # Implementation base
def debug_processor(): ...           # Debug utility

# __init__.pyi - Curated exports
class Processor: ...                 # EXPORTED - Primary interface
def create_processor() -> Processor: ... # EXPORTED - Construction
class ProcessorError(Exception): ... # EXPORTED - User-facing error

# Deliberately excluded:
# - ProcessorConfig: Use dict instead
# - validate_config: Internal validation  
# - ProcessorBase: Implementation detail
# - debug_processor: Not for production use
```

This demonstrates thoughtful interface curation.

## 9. Conformance

### 9.1 Specification Validation

API specifications MUST pass type checking and validate design quality:

**Type Checking Requirements**
- Pass `mypy --strict` without errors
- All exported names have complete annotations
- No undefined names referenced

**Completeness Checks**
- All exports are self-documented
- Examples demonstrate key usage patterns
- Behavioral guarantees are explicit

**Design Quality Metrics**  
- Export surface minimized
- Each export has single clear purpose
- Progressive complexity layers maintained
- Static analysis fully supported

### 9.2 Import Path Verification

Specifications MUST align with import patterns:

```python
# If users can do this:
from library import Thing
# Then library/__init__.pyi must define Thing

# If users can do this:  
from library.module import Other
# Then library/module.pyi must define Other
```

### 9.3 Tooling

Libraries SHOULD:
- Include `py.typed` marker for type checking
- Validate import paths match stub locations
- Test that public imports work as documented

### 9.4 Testing Specifications

Validate specifications through testing:

```python
# Test that exports match implementation
def test_exports_exist():
    from library import Process  # From stub
    assert hasattr(library, 'Process')  # In implementation

# Test behavioral contracts
def test_order_preservation():
    # Based on example in API spec
    results = batch_process([a, b, c])
    assert results[0].input == a  # Guaranteed by spec
```

## 10. Special Case Patterns

### 10.1 Properties

Properties require special documentation consideration:

**Read-Only Properties**
```python
@property
def name(self) -> str:
    """Entity name (read-only)."""
    ...
```

**Read-Write Properties**
```python
@property
def timeout(self) -> float:
    """Request timeout in seconds (0.1-300.0)."""
    ...

@timeout.setter
def timeout(self, value: float) -> None: ...
```

Export when properties provide the natural interface for attribute access.

### 10.2 Alternative Constructors

Class methods providing construction variants:

```python
@classmethod
def from_json(cls, data: str) -> Self:
    """
    Construct from JSON string.
    
    Args:
        data: Valid JSON matching expected schema
        
    Raises:
        JSONDecodeError: Invalid JSON
        ValidationError: Schema mismatch
    """
    ...
```

Always export alternative constructors that provide user-facing initialization.

### 10.3 Context Managers

Export when resource management is user-facing:

```python
def __enter__(self) -> Self:
    """Acquire connection and return self."""
    ...

def __exit__(self, *args: Any) -> None:
    """Release connection, never suppresses exceptions."""
    ...
```

### 10.4 Operator Overloading

Export operators only for types where they're naturally expected:

```python
# Good: Mathematical type
class Vector:
    def __add__(self, other: Vector) -> Vector:
        """Vector addition."""
        ...

# Avoid: Business object
class User:
    def __add__(self, other: User) -> User:  # Don't export
        ...
```

### 10.5 Overloaded Functions

Limit overloads to improve clarity:

```python
# Good: Clear distinction
@overload
def get(self, key: str) -> str: ...
@overload
def get(self, key: str, default: T) -> str | T: ...

# Avoid: Too many variants
@overload
def process(self, data: str) -> str: ...
@overload
def process(self, data: bytes) -> bytes: ...
@overload
def process(self, data: list[str]) -> list[str]: ...
# ... many more overloads
```

### 10.6 Async Patterns

Export async interfaces when I/O operations are involved:

```python
async def fetch(self, url: str) -> Response:
    """
    Fetch URL asynchronously.
    
    Must be awaited. Handles connection pooling internally.
    """
    ...
```

### 10.7 Type Variables and Generics

Document type relationships clearly:

```python
T = TypeVar('T')
"""Type variable for generic containers."""

K = TypeVar('K', bound=Hashable)
"""Hashable key type for mappings."""

class Container(Generic[T]):
    """
    Generic container for homogeneous items.
    
    Type parameter T is preserved through all operations.
    """
    def add(self, item: T) -> None: ...
    def get_all(self) -> list[T]: ...
```

## 11. API Evolution

### 11.1 Progressive Exposure Strategy

Start minimal, expand based on demonstrated need:

1. **Initial Release**: Export core functionality only
2. **User Feedback**: Identify missing conveniences
3. **Incremental Growth**: Add exports based on actual usage
4. **Avoid Speculation**: Don't export "might be useful" features

### 11.2 Stability Migration

Moving between tiers:

**Private → Public**: Remove underscore, document behavior
```python
# v1.0: _helper() is private
# v1.1: helper() becomes public (no stub yet)
```

**Public → Exported**: Add to stub with full documentation
```python
# v2.0: helper() added to stub (major version for new export)
```

**Exported → Deprecated**: Mark in stub, provide migration
```python
# v3.0: @deprecated("Use new_helper")
# v4.0: Removed from stub
# v5.0: Made private or removed entirely
```

### 11.3 Breaking Change Management

Handle breaking changes through clear communication:

```python
# v2.x - Add deprecation
@deprecated("Parameter 'old' renamed to 'new' in v3.0")
def function(old: str = None, new: str = None) -> None:
    """..."""

# v3.0 - Remove deprecated parameter
def function(new: str) -> None:
    """..."""
```

## 12. References

- PEP 484 - Type Hints
- PEP 561 - Distributing Type Information
- PEP 3119 - Protocol Classes
- RFC 2119 - Requirement Levels