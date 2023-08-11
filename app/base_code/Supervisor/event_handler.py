"""
Verifies that the event is enabled, runs the event and its action
"""
from . import Event, Events, EventKind
from . import supervisors_list
from .logger import log_error, log_state
from threading import Lock

def trigger_event(event: Event):
    """
    Trigger event
    """
    if not isinstance(event, Event):
        raise TypeError("event must be instance of Event")
    

    if not handle_event(event):
        return
    
    # run action.
    event.run_action()

    for event in get_enabled_controllable_events2():
        print(f"Automatic running event: {event.get_name()}")
        trigger_event(event)

# create a lock
lock = Lock()
def handle_event(event: Event):
    """
    Handle event
    """    
    if not isinstance(event, Event):
        raise TypeError("event must be instance of Event")
    #print(f"\n-----------------------------------------\nRunning event: {event.get_name()}")
    with lock:
        # print(f"Event: {event.get_name()}")
        execution_list = []
        for sup in supervisors_list:
            # verify if event is in Alphabet of supervisor
            # if not, ignore because the supervisor does not observe the event
            if event in sup.get_alphabet():
                # verify if event is enabled
                if event in sup.get_enabled_events():
                    # if enabled, add to execution list
                    execution_list.append(sup)
                else:
                    log_error(event, sup, f"Event not enabled")
                    return False

        # verify len of execution_list
        # if len is 0, no supervisor is observing the event
        if len(execution_list) == 0:
            log_error(f"Event {event.get_name()} not enabled")
            return False
        
        # run event
        for sup in execution_list:
            sup.run(event)
            log_state(event, [sup])
        return True


def get_enabled_controllable_events():
    """
    Get all enabled controllable events
    An event is enabled when it is present in the supervisor alphabet
    AND enabled in the current state.
    """
    enabled_controllable_events = []
    # get enabled events on first supervisor
    enabled_controllable_events = supervisors_list[0].get_enabled_controllable_events()
    # get intersection of controllable events on other supervisors
    for sup in supervisors_list[1:]:
        # get alphabet of the supervisor
        sup_alphabet = sup.get_alphabet()
        # get enabled controllable events of the supervisor
        sup_enabled_controllable_events = sup.get_enabled_controllable_events()
        # get intersection
        # iterate over a copy of the list
        # Iterating over this copy allows safely remove elements 
        # from the original list without affecting the iteration.
        for event in enabled_controllable_events[:]:
            if event in sup_alphabet:
                if event not in sup_enabled_controllable_events:
                    enabled_controllable_events.remove(event)
    
    if(len(enabled_controllable_events) > 0):
        print("Controllable events enabled: [", end="")
        for event in enabled_controllable_events:
            print(event.get_name(), end=", ")
        # remove last ", "
        print("\b\b", end="")
        print("]")

    return enabled_controllable_events


def get_enabled_controllable_events2():
    """
    Get all enabled controllable events
    An event is enabled when it is present in the supervisor alphabet
    AND enabled in the current state.
    """

    # get all Controllable events on Events, using contraction
    controllable_events = [event for event in Events.values() if event.get_kind() == EventKind.CONTROLLABLE]

    # get intersection of controllable events on other supervisors
    for sup in supervisors_list:
        # get intersection
        # iterate over a copy of the list
        # Iterating over this copy allows safely remove elements 
        # from the original list without affecting the iteration.
        for event in controllable_events[:]:
            if event in sup.get_alphabet():
                if event not in sup.get_enabled_controllable_events():
                    controllable_events.remove(event)
    
    if(len(controllable_events) > 0):
        print("Controllable events enabled: [", end="")
        for event in controllable_events:
            print(event.get_name(), end=", ")
        # remove last ", "
        print("\b\b", end="")
        print("]")

    return controllable_events
