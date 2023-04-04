# DESPythonMaker

This tool can parse a "Waters/Supremica" file (.wmod) and generate a Python code with the same structure of the inside supervisors and distinguishers.

The code generated is independent and don't any requeriment.

# Pre-requisites

## Windows

Install python3.

Open Powershell as administrator and run:
```powershell
Set-ExecutionPolicy Unrestricted
```
Select 'Y' and press enter.

run ```setup_win.ps1``` with Powershell to create virtual environment and install dependencies.

<span style="color:red">Or use WSL and be free and happy.</span>

## Linux
run ```setup_linux.sh``` with bash to create virtual environment and install dependencies.

## Supremica
 For convenience, when synthesizing a supervisor, mark the 'Rename states' option.
- Before send supervisor 'To editor', 'Rename automaton' to remove caracteres and spaces. Keep only letters and numbers.
- Do not name a supervisor as 'supervisor'
- The name of all distinguishers MUST start with GD. For example, GD1, GD2, GDwhatever, etc.
- As one would anticipate, it is imperative that no other components bear nomenclature commencing with 'GD'.

# Generate code

## Windows

run `app\despythonmaker.ps1 -i <input> -o <output> -e <y/n>` with Powershell to execute the software:
-  `-i <input>`: input file (required)
-  `-o <output>`: output directory. Default: 'generated_code'
-  `-e` : execute the generated code. Default: y
 
## Linux

run `app\despythonmaker.sh -i <input> -o <output> -e -h` with terminal to execute the software:
- `-i <input>` : input file (required)
- `-o <output>` : output directory. Default: generated_code
- `-e` : execute the generated code. Default: y
- `-h` : help

The script will generate a structure with the same name of the output directory. The folder will contain the generated code, organized in the same structure of the `base_code`. Inside generated code also will be a `README.md` with the instructions to run the code. Now, this can be readed in `app/base_code/README.md`.

# How to use

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


# cite this work
If you use this software, please cite this work:
```bibtex
@software{Possato_DESPythonMaker_2023,
author = {Possato, Tiago and Valentini, João Henrique and Lapa, Hudson},
license = {GPL-3.0+},
month = {3},
title = {{DESPythonMaker}},
url = {https://github.com/tiagopossato/des_python_maker},
year = {2023}
}
```
