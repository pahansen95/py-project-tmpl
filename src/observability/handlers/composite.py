"""
Composite handlers for event distribution.

Handlers that coordinate multiple sub-handlers.
"""

from typing import List
import asyncio

from ..types import EventDict, EventHandler
from .base import get_handler_name, safe_handler_call


class FanoutHandler:
    """Broadcast events to multiple handlers with lifecycle support."""
    
    def __init__(self, *handlers: EventHandler):
        self.handlers = list(handlers)
    
    async def initialize(self) -> None:
        """Initialize all sub-handlers."""
        tasks = []
        for handler in self.handlers:
            if hasattr(handler, 'initialize'):
                tasks.append(handler.initialize())
        
        if tasks:
            await asyncio.gather(*tasks, return_exceptions=True)
    
    async def shutdown(self) -> None:
        """Shutdown all sub-handlers."""
        tasks = []
        for handler in self.handlers:
            if hasattr(handler, 'shutdown'):
                tasks.append(handler.shutdown())
        
        if tasks:
            await asyncio.gather(*tasks, return_exceptions=True)
    
    def __call__(self, event: EventDict) -> None:
        """Forward event to all handlers."""
        for handler in self.handlers:
            try:
                handler(event)
            except Exception as e:
                safe_handler_call(f"fanout.{get_handler_name(handler)}", "processing", e)


class FallbackHandler:
    """Try handlers in order until one succeeds."""
    
    def __init__(self, primary: EventHandler, *backups: EventHandler):
        self.primary = primary
        self.backups = list(backups)
        self.all_handlers = [primary] + self.backups
    
    async def initialize(self) -> None:
        """Initialize all handlers."""
        tasks = []
        for handler in self.all_handlers:
            if hasattr(handler, 'initialize'):
                tasks.append(handler.initialize())
        
        if tasks:
            await asyncio.gather(*tasks, return_exceptions=True)
    
    async def shutdown(self) -> None:
        """Shutdown all handlers."""
        tasks = []
        for handler in self.all_handlers:
            if hasattr(handler, 'shutdown'):
                tasks.append(handler.shutdown())
        
        if tasks:
            await asyncio.gather(*tasks, return_exceptions=True)
    
    def __call__(self, event: EventDict) -> None:
        """Try handlers until one succeeds."""
        # Try primary first
        try:
            self.primary(event)
            return
        except Exception as e:
            safe_handler_call(f"fallback.primary.{get_handler_name(self.primary)}", "processing", e)
        
        # Try backups in order
        for i, handler in enumerate(self.backups):
            try:
                handler(event)
                return  # Success
            except Exception as e:
                safe_handler_call(f"fallback.backup[{i}].{get_handler_name(handler)}", "processing", e)
        
        # All handlers failed
        if __debug__:
            import sys
            print(f"All handlers failed for event type: {event.get('type', 'unknown')}", file=sys.stderr)
        Handler with fallback behavior
    """
    fall = FallbackHandler(primary, *backups)
    
    def wrapper(event: EventDict) -> None:
        fall(event)
    
    # Create readable name
    all_names = [get_handler_name(primary)] + [get_handler_name(h) for h in backups]
    wrapper.__name__ = f"fallback({' -> '.join(all_names)})"
    wrapper.initialize = fall.initialize
    wrapper.shutdown = fall.shutdown
    
    return wrapper