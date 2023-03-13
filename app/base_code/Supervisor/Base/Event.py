from enum import Enum

class EventKind(Enum):
    CONTROLLABLE = 0
    UNCONTROLLABLE = 1

class Event:
    def __init__(self, kind: EventKind, event_id: int, name: str):
        if not isinstance(kind, EventKind):
            raise TypeError("kind must be instance of EventKind")
        if not isinstance(event_id, int):
            raise TypeError("event_id must be an integer")

        self.__kind = kind
        self.__event_id = event_id
        self.__name = name
        self.__callback = None
    
    def get_kind(self) -> EventKind:
        return self.__kind
    
    def get_name(self) -> str:
        return self.__name
    
    def get_id(self) -> int:
        return self.__event_id

    def set_callback(self, callback):
        self.__callback = callback
    
    def run_callback(self):
        if self.__callback is not None:
            self.__callback(self)