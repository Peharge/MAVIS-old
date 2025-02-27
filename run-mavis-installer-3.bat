@echo off
setlocal enabledelayedexpansion

echo MAVIS Installer 3
echo -----------------

:: Function to check if Python is installed
:check_python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python 3.12 is not installed.
    set /p install_python="Would you like to install Python 3.12? (y/n): "
    if /i "%install_python%"=="y" (
        echo Downloading and installing Python 3.12...
        start https://www.python.org/downloads/release/python-3120/
    ) else (
        echo Python installation aborted.
    )
) else (
    echo Python 3.12 is already installed.
)

:: Function to check if Git is installed
:check_git
git --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Git is not installed.
    set /p install_git="Would you like to install Git? (y/n): "
    if /i "%install_git%"=="y" (
        echo Downloading and installing Git...
        start https://git-scm.com/download/win
    ) else (
        echo Git installation aborted.
    )
) else (
    echo Git is already installed.
)

:: Function to check if Ollama is installed
:check_ollama
ollama --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Ollama is not installed.
    set /p install_ollama="Would you like to install Ollama? (y/n): "
    if /i "%install_ollama%"=="y" (
        echo Downloading and installing Ollama...
        start https://ollama.com/download
    ) else (
        echo Ollama installation aborted.
    )
) else (
    echo Ollama is already installed.
)

:: Create PyCharm Projects folder if it doesn't exist
set "pycharm_projects=%USERPROFILE%\PycharmProjects"
if not exist "%pycharm_projects%" (
    echo Creating folder %pycharm_projects%...
    mkdir "%pycharm_projects%"
)

:: Change to PyCharm Projects directory
cd /d "%pycharm_projects%"

:: Check if MAVIS folder exists, if not, clone it
if not exist "%pycharm_projects%\MAVIS" (
    echo Cloning MAVIS repository from GitHub...
    git clone https://github.com/Peharge/MAVIS.git
) else (
    echo MAVIS already exists.
)

:: Change to MAVIS directory
cd /d "%pycharm_projects%\MAVIS"

:: Create .env file if it doesn't exist
if not exist ".env" (
    echo Creating .env file...
    echo # Environment variables for MAVIS > .env
    echo PYTHONPATH=%pycharm_projects%\MAVIS >> .env
) else (
    echo .env file already exists.
)

:: Execute run-mavis-3-all.bat if it exists
if exist "%pycharm_projects%\MAVIS\run-mavis-3-all.bat" (
    echo Starting run-mavis-3-all.bat...
    call "%pycharm_projects%\MAVIS\run-mavis-3-all.bat"
) else (
    echo run-mavis-3-all.bat not found. Please ensure the file path is correct.
)

:: Completion
echo All tasks have been completed.
pause
exit
