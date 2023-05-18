from Event import Event
from Transition import Transition

class State:
    def __init__(self, name: str, is_start: bool = False):
        self.__is_start = is_start
        self.__name = name
        self.__transitions = []
    
    def add_transition(self, event: Event, target: "State"):


        if self.get_transition(event, target) is None:
            self.__transitions.append(Transition(event, target))
        else:
            print(f"Transition from state {self.name} to state {target.get_name()} \
                    with the event {event.get_name()} already exists.")

    def get_transition(self, event: Event, target):
     
        for transition in self.__transitions:
            if transition.get_event() == event and transition.get_target() == target:
                return transition
        return None

    def get_transitions(self):
        return self.__transitions
    
    def get_name(self) -> str:
        return self.__name
    
    def is_start(self) -> bool:
        return self.__is_start