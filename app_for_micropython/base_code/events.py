from Event import Event

CONTROLLABLE = 0
UNCONTROLLABLE = 1

# Create events
Events = {
    'btn': Event(UNCONTROLLABLE, 0, 'btn'),
    'liga': Event(CONTROLLABLE, 1, 'liga'),
    'desliga': Event(CONTROLLABLE, 2, 'desliga'),
}

def get_event_by_id(event_id):
    """
    Get event by id
    """
    for event in Events.values():
        if event.get_id() == event_id:
            return event
    return None