from Event import Event
import State

class Transition:
    def __init__(self, event: Event, target: State):
        self.__event = event
        self.__target = target
    
    def get_event(self) -> Event:
        return self.__event
    
    def get_target(self) -> State:
        return self.__target