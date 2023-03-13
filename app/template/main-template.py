from Supervisor import Events, Event, handle_event

def default_callback(event: Event):
    """
    Default callback for example
    """
    print(f"Default callback for event {event.get_name()}")

# set default callback for example
%$%{set_callback}

if __name__ == '__main__':
    # handle events for teste
%$%{handle_event}