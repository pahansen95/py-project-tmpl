from typing import Optional, Any
import threading
import sys
import atexit

from .core import ObservabilityConfig, ObservabilityContext
from .handlers.sink import PrintHandler


class SharedContext:
  """Singleton providing a shared observability context."""

  _ctx: Optional[ObservabilityContext] = None
  _lock: threading.Lock = threading.Lock()
  _cleanup_registered: bool = False

  @classmethod
  def setup(cls, config: Optional[ObservabilityConfig] = None) -> None:
    """Initialize the shared context.

    Args:
        config: Optional configuration. If None, uses default stderr output.

    Raises:
        RuntimeError: If already initialized.
    """
    with cls._lock:
      if cls._ctx is not None:
        raise RuntimeError("Shared context already initialized. Call teardown() before reinitializing.")

      # Use provided config or create default
      if config is None:
        config = ObservabilityConfig(handlers=[PrintHandler(sys.stderr)], sampling_rate=1.0)

      # Create and start context
      cls._ctx = ObservabilityContext(config)
      cls._ctx.start()

      # Register cleanup only once
      if not cls._cleanup_registered:
        atexit.register(cls.teardown)
        cls._cleanup_registered = True

  @classmethod
  def get(cls) -> ObservabilityContext:
    """Get the shared context.

    Returns:
        The shared context instance.

    Raises:
        RuntimeError: If not initialized.
    """
    if cls._ctx is None:
      raise RuntimeError("Shared context not initialized. Call SharedContext.setup() first.")
    return cls._ctx

  @classmethod
  def teardown(cls) -> None:
    """Explicitly teardown the shared context."""
    with cls._lock:
      if cls._ctx is not None:
        cls._ctx.shutdown()
        cls._ctx = None

  @classmethod
  def emit(cls, event_type: str, value: Any, **metadata) -> None:
    """Emit event using the shared context.

    Convenience method that delegates to the context.
    """
    cls.get().emit(event_type, value, **metadata)
