# Code maker

This project can parse a Supremica file (.wmod) and generate a Python 3 code with the same structure of the inside supervisors.

The code generated is independent and don't any requeriment.

# How to use

## Pre-requisites

### Ambient

run `env_setup.sh` to creat an virtual environment and install the requeriments.

### Supremica
- For convenience, when synthesizing a supervisor, mark the 'Rename states' option.
- Before send supervisor 'To editor', 'Rename automaton' to remove caracteres and spaces. Keep only letters and numbers. It's recommended follow the patterns in https://peps.python.org/pep-0008/#naming-conventions

## Generate code

- Use the script `./run.sh` to call the python code `maker.py`.
    - Usage: `./run.sh -i <input> -o <output> -e -h`
    - `-i <input>` : input file (required)
    - `-o <output>` : output directory. Default: generated_code
    - `-e` : if present, execute the generated code. Default: no execution
    - `-h` : help

The script will generate a folder with the same name of the output directory. The folder will contain the generated code, organized in the same structure of the `base_code`. Inside generated code also will be a `README.md` with the instructions to run the code. Now, this can be readed in `template\README.md`.

# Adding path to the system
add the following line to your `~/.bashrc` file:

```bash
export PATH=$PATH:/path-to-project/code-maker/maker-python
```
than run `source ~/.bashrc` to reload the file.
