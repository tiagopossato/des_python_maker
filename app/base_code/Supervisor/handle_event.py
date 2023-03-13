"""
Verifies that the event is enabled, runs the event and its callback
"""
from . import Event
from .supervisors import sup
from .logger import log_error, log_state
from threading import Lock

supervisors = [sup]

# create a lock
lock = Lock()
def handle_event(event: Event):
    """
    Handle event
    """
    # verify if event is in Events dictionary
    if not isinstance(event, Event):
        raise TypeError("event must be instance of Event")
    with lock:
        # print(f"Event: {event.get_name()}")
        execution_list = []
        for sup in supervisors:
            # if event is in supervisor alphabet
            if event in sup.get_alphabet():
                # verify if event is enabled
                if event in sup.get_enabled_events():
                    execution_list.append(sup)
                else:
                    log_error(event, sup, f"Event not enabled")
                    return

        # verify len of execution_list
        # if 0, event is not in any supervisor alphabet
        if len(execution_list) == 0:
            print(f"Event {event.get_name()} not enabled")
            return
        
        # run event
        for sup in execution_list:
            sup.run(event)

        log_state(event, supervisors)
    # run callback.
    # Must be the last thing to do
    # and must be outside the lock
    # because it can change the state
    # and call another handle_event
    event.run_callback()