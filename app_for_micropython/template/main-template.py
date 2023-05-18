from events import Events
from Event import Event
from handle_event import handle_event

def default_action(event: Event):
    """
    Default action for example
    """
    print(f"Default action for event {event.get_name()}")

# set default action for example
%$%{set_action}

if __name__ == '__main__':
    # handle events for teste
%$%{handle_event}