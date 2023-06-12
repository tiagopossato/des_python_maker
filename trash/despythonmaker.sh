#!/usr/bin/env bash

# script para rodar criar as pastas de saída, movimentar os arquivos base e rodar o maker.py

BASEDIR="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"

source "$BASEDIR"/../env/bin/activate

unset -v input
unset -v output
unset -v exec

output=generated_code
exec="N"

# function to print help
function print_help {
    echo "Usage: run.sh -i <input> -o <output> -e"
    echo " -i <input>: input file (required)"
    echo " -o <output>: output directory. Default: generated_code"
    echo " -e: if present, execute the generated code. Default: no execution"
    echo " -h: help"
}

# verify if user set params
if [ $# -eq 0 ]; then
    print_help
    exit 0
fi

# Get the options.
shift "$(( OPTIND - 1 ))"
while getopts i:o:eh option; do
#print passed options
    case $option in
        h) 
            print_help
            exit 0
            ;;
        i)
            input=$OPTARG   
            # echo "input file: $input"
            ;;
        o)
            output=$OPTARG
            # echo "output file: $output"
            ;;
        e)
            exec="y"
            # echo "executing after generation"
            ;;
        \?)
            echo "Invalid option: -$OPTARG" >&2
            exit 1
            ;;
    esac
done

# check if the value of the input variable is set. 

if [ -z "$input" ]; then
        print_help
        exit 1
fi

# verify if output directory exists
if [ -d "$output" ]; then
    read -p "Output directory exists. Do you want to overwrite it? [y/n] " -n 1 -r
    echo    # (optional) move to a new line
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        rm -rf "$output"
    else
        exit 1
    fi
fi

# copy base code to output directory
# "Supervisor/supervisors/sup.py" is excluded because it is a example of a supervisor. Other example files are subscribed by the maker.py script
rsync -ar --exclude '*template*' --exclude '__pycache__' --exclude 'Supervisor/supervisors/sup.py' "$BASEDIR/base_code/" "$output/"

# run the main script and capture the output
python3 "$BASEDIR"/maker.py --input="$input" --output="$output"

# execute if user wants and if the generation was successful
if [ $? -eq 0 ]; then
    echo "Generation successful"
    if [ "$exec" == "y" ]; then
        # clear the screen
        # clear
        cd "$output"
        python3 main.py
fi

else
    echo "Generation failed"
    exit 1
fi
