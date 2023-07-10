"""
Verifies that the event is enabled, runs the event and its action
"""
from Event import Event
from sup import sup

supervisors_list = [sup]

def handle_event(event: Event):
    """
    Handle event
    """    
    if not isinstance(event, Event):
        raise TypeError("event must be instance of Event")
    print(f"\n-----------------------------------------\nRunning event: {event.get_name()}")

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
                print(f"Event {event.get_name()} not enabled")
                return

    # verify len of execution_list
    # if len is 0, no supervisor is observing the event
    if len(execution_list) == 0:
        print(f"Event {event.get_name()} not enabled")
        return
    
    # run event
    for sup in execution_list:
        sup.run(event)
        transtion = f"{sup.get_name()}: {sup.get_last_state().get_name()} -> {sup.get_current_state().get_name()}"
        print(f"Event {event.get_name()} > {transtion}")
    # print_enabled_controllable_events()
    # run action.
    # It must be the last thing to do
    # for no cause a deadlock
    # because it can change the state
    # and call another handle_event
    event.run_action()
    for event in get_enabled_controllable_events():
        print(f"Automatic running event: {event.get_name()}")
        handle_event(event)

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
