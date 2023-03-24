@echo off

echo Verificando instalação do Python3...

where python >nul 2>nul

if %errorlevel% == 0 (
    echo Python3 já está instalado.
) else (
    echo Python3 não está instalado.

    echo Detectando arquitetura do computador...

    set "PROCESSOR_ARCHITECTURE="

    if "%PROCESSOR_ARCHITECTURE%" == "x86" (
        echo Arquitetura do computador: 32 bits

        echo Baixando o Python versão 3.11.2...
        powershell -Command "(New-Object Net.WebClient).DownloadFile('https://www.python.org/ftp/python/3.11.2/python-3.11.2.exe', 'python_installer.exe')"

    ) else if "%PROCESSOR_ARCHITECTURE%" == "AMD64" (
        echo Arquitetura do computador: 64 bits

        echo Baixando o Python versão 3.11.2...
        powershell -Command "(New-Object Net.WebClient).DownloadFile('https://www.python.org/ftp/python/3.11.2/python-3.11.2-amd64.exe', 'python_installer.exe')"        
    ) else (
        echo Não foi possível detectar a arquitetura do computador.
        echo Instale o Python3 manualmente e execute o script novamente.
        goto :EOF
    )

    echo Instalando o Python...
    python_installer.exe /quiet InstallAllUsers=1 PrependPath=1
    echo Removendo arquivo de instalação...
    del python_installer.exe
    echo Script concluído.
)

echo Criando ambiente virtual...

python -m venv env

echo Ativando ambiente virtual...

.\env\Scripts\activate.bat

echo Instalando dependências...

pip install -r requirements.txt

echo Script concluído.
