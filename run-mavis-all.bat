@echo off

set USERNAME=%USERNAME%
set PYTHON_PATH=C:\Users\%USERNAME%\PycharmProjects\MAVIS\.env\Scripts\python.exe
set SCRIPT_PATH_1=C:\Users\%USERNAME%\PycharmProjects\MAVIS\main\main.py

if not exist "%PYTHON_PATH%" (
    echo Error: Python interpreter not found: %PYTHON_PATH%
    exit /B 1
)

if not exist "%SCRIPT_PATH_1%" (
    echo Error: Script not found: %SCRIPT_PATH_1%
    exit /B 1
)

"%PYTHON_PATH%" "%SCRIPT_PATH_1%"

echo.
echo The scripts have been executed, Ollama has been started, and the browser has been opened.
echo Press any key to exit.
pause