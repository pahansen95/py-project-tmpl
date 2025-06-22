"""
Configuration types for observability system.

Provides immutable configuration structures that define the observability
setup at initialization time. Configuration flows from application boundaries
inward, replacing runtime mutation with declarative setup.
"""

from dataclasses import dataclass, field
from typing import List, Set

from .types import EventHandler


@dataclass(frozen=True)
class ObservabilityConfig:
  """
  Immutable configuration for observability context.

  Defines all aspects of observability behavior at initialization time.
  Runtime mutation is not supported - create a new context for different
  configuration.
  """

  handlers: List[EventHandler] = field(default_factory=list)
  sampling_rate: float = 1.0
  enabled_categories: Set[str] = field(default_factory=set)

  def __post_init__(self):
    """Validate configuration."""
    if not 0.0 <= self.sampling_rate <= 1.0:
      raise ValueError(f"Sampling rate must be between 0 and 1, got {self.sampling_rate}")


def create_observability(config: ObservabilityConfig) -> "ObservabilityContext":
  """
  Factory function to create configured observability context.

  Args:
      config: Configuration to apply

  Returns:
      Configured ObservabilityContext instance
  """
  from .context import ObservabilityContext

  context = ObservabilityContext(config)

  # Attach handlers directly from config
  for handler in config.handlers:
    context.attach_handler(handler)

  return context
