@echo off

set USERNAME=%USERNAME%
set PYTHON_PATH=C:\Users\%USERNAME%\PycharmProjects\MAVIS\.env\Scripts\python.exe
set SCRIPT_PATH_1=C:\Users\%USERNAME%\PycharmProjects\MAVIS\info.py
set SCRIPT_PATH_2=C:\Users\%USERNAME%\PycharmProjects\MAVIS\mavis-1-2-main-mini-mini.py
set PYTHON_SCRIPT_PATH=C:\Users\%USERNAME%\PycharmProjects\MAVIS\run_with_browser.py

:: Check if the Python interpreter exists
if not exist "%PYTHON_PATH%" (
    echo Error: Python interpreter not found: %PYTHON_PATH%
    exit /B 1
)

:: Check if the Python script for starting Ollama exists
if not exist "%PYTHON_SCRIPT_PATH%" (
    echo Error: Python script not found: %PYTHON_SCRIPT_PATH%
    exit /B 1
)

:: Start the Python script to launch Ollama and open the browser
"%PYTHON_PATH%" "%PYTHON_SCRIPT_PATH%"

:: Check if the first Python script exists
if not exist "%SCRIPT_PATH_1%" (
    echo Error: Script not found: %SCRIPT_PATH_1%
    exit /B 1
)

"%PYTHON_PATH%" "%SCRIPT_PATH_1%"

:: Check if the second Python script exists
if not exist "%SCRIPT_PATH_2%" (
    echo Error: Script not found: %SCRIPT_PATH_2%
    exit /B 1
)

"%PYTHON_PATH%" "%SCRIPT_PATH_2%"

echo.
echo The scripts have been executed, Ollama has been started, and the browser has been opened.
echo Press any key to exit.
pause