
CONTROLLABLE = 0
UNCONTROLLABLE = 1

class Event:
    def __init__(self, kind, event_id: int, name: str):
        if not isinstance(event_id, int):
            raise TypeError("event_id must be an integer")

        self.__kind = kind
        self.__event_id = event_id
        self.__name = name
        self.__action = None
    
    def get_kind(self):
        return self.__kind
    
    def is_controllable(self) -> bool:
        return self.__kind == CONTROLLABLE
    
    def get_name(self) -> str:
        return self.__name
    
    def get_id(self) -> int:
        return self.__event_id

    def set_action(self, action):
        self.__action = action
    
    def run_action(self):
        if self.__action is not None:
            self.__action(self)