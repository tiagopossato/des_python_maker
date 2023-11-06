# DESPythonMaker

This tool can parse a "Waters/Supremica" file (.wmod) and generate a Python code with the same structure of the inside supervisors and distinguishers.

The code generated is independent and don't any requeriment.

# Pre-requisites

Install python3.

## Supremica
- For convenience, when synthesizing a supervisor, mark the 'Rename states' option.
- Before send supervisor 'To editor', 'Rename automaton' to remove caracteres and spaces. Keep only letters and numbers.
- Do not name a supervisor as 'supervisor'
- The name of all distinguishers MUST start with GD. For example, GD1, GD2, GDwhatever, etc.
- As one would anticipate, it is imperative that no other components bear nomenclature commencing with 'GD'.

# Generating code

run `python3 app\despythonmaker.py -i <input> -o <output> -e` with terminal to execute the software:
- `-i <input>` : input file (required)
- `-o <output>` : output directory. Default: generated_code
- `-e` : if present, compile with cmake/gcc and execute the generated code. Default: no execution

In the first execution, the script will create the virtual environment and install the dependencies. This can take a while. After that, the script will generate the code.

The script will generate a structure with the same name of the output directory. The folder will contain the generated code, organized in the same structure of the `base_code`. Inside generated code also will be a `README.md` with the instructions to run the code. Now, this can be readed in `app/base_code/README.md`.

# Usage example

The repository [DESPythonMaker Usage Example](https://github.com/tiagopossato/des_python_maker_example)  contains a use case example.

# How to use the generated code

The file `main.py` is the entry point of the generated code and the only file you need to change and run.

1. First, create a action function to be called by the event handler whenever a handled event is enabled. The action function must have the following signature:

    ```python
    def action(event: Event):
        # do something
    ```
    Note that the action function receives an event as its parameter, which is an object belonging to the Event class. This particular event is the one that was enabled in the supervisor and subsequently triggered the invocation of the action function.

    In the action function, you can trigger other events by calling the `trigger_event` function.:

    ```python
    trigger_event(Events['other_event_name'])
    ```

2. Then, set the action function to the event handler:

    ```python
    Events['event_name'].set_action(action)
    ```

3. Finally, when an event is received, run the event handler:

    ```python
    trigger_event(Events['event_name'])
    ```

    If the event is enabled in all supervisors, the action function will be called.


# cite this work
If you use this software, please cite this work. View citation in "Cite this repository"
