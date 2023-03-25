# Generated code


The file `main.py` is the entry point of the generated code and the only file you need to change and run.

1. First, create a callback function to be called by the event handler whenever a handled event is enabled. The callback function must have the following signature:

    ```python
    def callback(event: Event):
        # do something
    ```
    Note that the callback function receives an event as its parameter, which is an object belonging to the Event class. This particular event is the one that was enabled in the supervisor and subsequently triggered the invocation of the callback function.

    In the callback function, you can trigger other events by calling the `handle_event` function.:

    ```python
    handle_event(Events['other_event_name'])
    ```

2. Then, set the callback function to the event handler:

    ```python
    Events['event_name'].set_callback(callback)
    ```

3. Finally, when an event is received, run the event handler:

    ```python
    handle_event(Events['event_name'])
    ```

    If the event is enabled in all supervisors, the callback function will be called.

`Events` is a dictionary with all the events. This is defined in the file `Supervisor/events.py`.