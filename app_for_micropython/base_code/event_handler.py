"""
Verifies that the event is enabled, runs the event and its action
"""
from Event import Event, CONTROLLABLE
from events import Events
from sup import sup

supervisors_list = [sup]

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

    # get all Controllable events on Events, using contraction
    controllable_events = [event for event in Events.values() if event.get_kind() == CONTROLLABLE]

    for event in controllable_events:
        #print(f"Automatic running event: {event.get_name()}")
        trigger_event(event)


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
                #print(f"Event {event.get_name()} not enabled")
                return False

    # verify len of execution_list
    # if len is 0, no supervisor is observing the event
    if len(execution_list) == 0:
        print(f"Event {event.get_name()} not enabled")
        return False
    
    # run event
    for sup in execution_list:
        sup.run(event)
        transtion = f"{sup.get_name()}: {sup.get_last_state().get_name()} -> {sup.get_current_state().get_name()}"
        print(f"Event {event.get_name()} > {transtion}")
    
    return True
