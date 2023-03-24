"""
Verifies that the event is enabled, runs the event and its callback
"""
from . import Event
from .supervisors import %$%{supervisor_list}
from .logger import log_error, log_state
from threading import Lock

supervisors = [%$%{supervisor_list}]

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
            if event in sup.get_alphabet():
                if event not in sup.get_enabled_events():
                    log_error(event, sup, f"Event not enabled")
                    return
                else:
                    execution_list.append(sup)

        # verify len of execution_list
        if len(execution_list) == 0:
            print(f"Event {event.get_name()} not enabled")
            return
        
        # run event
        for sup in execution_list:
            sup.run(event)
            log_state(event, [sup])
    # run callback.
    # Must be the last thing to do
    # and must be outside the lock
    # because it can change the state
    # and call another handle_event
    event.run_callback()