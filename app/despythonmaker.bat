@echo off

set "BASEDIR=%~dp0"

call "%BASEDIR%\..\env\Scripts\activate.bat"

set "input="
set "output=generated_code"
set "exec=N"

REM function to print help
:print_help
echo Usage: run.bat -i input -o output -e
echo  -i input: input file (required)
echo  -o output: output directory. Default: generated_code
echo  -e: if present, execute the generated code. Default: no execution
echo  -h: help
goto :EOF

REM verify if user set params
if "%~1"=="" goto print_help

REM Get the options
:parse_options
shift
if "%~1"=="" goto execute

set "option=%~1"
if "%~2"=="" goto :print_help
set "value=%~2"

if /i "%option%"=="-h" goto print_help
if /i "%option%"=="-i" set "input=%value%"
if /i "%option%"=="-o" set "output=%value%"
if /i "%option%"=="-e" set "exec=Y"

goto parse_options

:execute
REM check if the value of the input variable is set
if "%input%"=="" goto :print_help

REM verify if output directory exists
if exist "%output%" (
    set /p "overwrite=Output directory exists. Do you want to overwrite it? [y/n] "
    if /i "%overwrite%"=="y" (
        rmdir /s /q "%output%"
    ) else (
        exit /b 1
    )
)

REM print the options
echo Input file: %input%
echo Output directory: %output%
echo Script location: %BASEDIR%


REM copy base code to output directory
REM "Supervisor/supervisors/sup.py" is excluded because it is a example of a supervisor. Other example files are subscribed by the maker.py script
REM copy base code to output directory

xcopy /E /exclude:"$BASEDIR\base_code\*template*" /exclude:"$BASEDIR\base_code\__pycache__\" /exclude:"$BASEDIR\base_code\Supervisor\supervisors\sup.py" "$BASEDIR\base_code\" "$output\"

REM run the main script and capture the output
python "%BASEDIR%\maker.py" --input="%input%" --output="%output%"

REM execute if user wants and if the generation was successful
if %errorlevel% equ 0 (
    echo Generation successful
    if /i "%exec%"=="Y" (
        REM clear the screen
        cls
        cd "%output%"
        call run.bat
    )
) else (
    echo Generation failed
    exit /b 1
)
