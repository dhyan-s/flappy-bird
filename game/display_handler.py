import pygame

class DisplayHandler:
    """
    A class that handles the display and management of different screens in a pygame application.
    """
    
    def __init__(self) -> None:
        self._states: dict[str, type[object]] = {}
        self._current_state: str = None
        
    def add_state(self, state_name: str, state_class: type[object]) -> None:
        """Adds a new state to the DisplayHandler."""
        self._states[state_name] = state_class
        
    def remove_state(self, state_name: str) -> None:
        """Removes a state from the DisplayHandler."""
        self._states.pop(state_name, None)
        if self._current_state == state_name:
            self._current_state = None
            
    def set_current_state(self, state_name: str) -> None:
        """Sets the current active screen."""
        if state_name in self._states:
            self._current_state = state_name
            if callable(getattr(self._states[self._current_state], "on_set_active", None)):
                self._states[self._current_state].on_set_active()
        
    def render(self) -> None:
        """Renders the active screen"""
        if self._current_state is not None and self._current_state in self._states:
            self._states[self._current_state].render()
            
    def handle_event(self, event: pygame.event.Event) -> None:
        """Calls the handle_event() method of the active state."""
        if self._current_state is not None and self._current_state in self._states:
            self._states[self._current_state].handle_event(event)
