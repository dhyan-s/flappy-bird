import pygame

class DisplayHandler:
    def __init__(self) -> None:
        self._states: dict[str, type[object]] = {}
        self._current_state: str = None
        
    def add_state(self, state_name: str, state_class: type[object]) -> None:
        self._states[state_name] = state_class
        
    def remove_state(self, state_name: str) -> None:
        self._states.pop(state_name, None)
        if self._current_state == state_name:
            self._current_state = None
            
    def set_current_state(self, state_name: str) -> None:
        if state_name in self._states:
            self._current_state = state_name
            if callable(getattr(self._states[self._current_state], "on_set_active", None)):
                self._states[self._current_state].on_set_active()
        
    def render(self) -> None:
        if self._current_state is not None and self._current_state in self._states:
            self._states[self._current_state].render()