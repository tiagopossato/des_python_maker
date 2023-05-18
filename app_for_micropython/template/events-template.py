from Event import Event

CONTROLLABLE = 0
UNCONTROLLABLE = 1

# Create events
Events = {
%$%{events}}

def get_event_by_id(event_id):
    """
    Get event by id
    """
    for event in Events.values():
        if event.get_id() == event_id:
            return event
    return None