@echo off

set USERNAME=%USERNAME%
set PYTHON_PATH=C:\Users\%USERNAME%\PycharmProjects\MAVIS\.env\Scripts\python.exe
set SCRIPT_PATH_1=C:\Users\%USERNAME%\PycharmProjects\MAVIS\info.py
set SCRIPT_PATH_2=C:\Users\%USERNAME%\PycharmProjects\MAVIS\mavis-1-2-main-main.py
set OLLAMA_PATH=C:\Users\%USERNAME%\AppData\Local\Programs\Ollama\ollama app.exe

if not exist "%PYTHON_PATH%" (
    echo Fehler: Python-Interpreter nicht gefunden: %PYTHON_PATH%
    exit /B 1
)

if not exist "%SCRIPT_PATH_1%" (
    echo Fehler: Skript nicht gefunden: %SCRIPT_PATH_1%
    exit /B 1
)

"%PYTHON_PATH%" "%SCRIPT_PATH_1%"

if not exist "%SCRIPT_PATH_2%" (
    echo Fehler: Skript nicht gefunden: %SCRIPT_PATH_2%
    exit /B 1
)

"%PYTHON_PATH%" "%SCRIPT_PATH_2%"

if not exist "%OLLAMA_PATH%" (
    echo Fehler: Ollama nicht gefunden: %OLLAMA_PATH%
    exit /B 1
)

start "" "%OLLAMA_PATH%"

echo.
echo Die Skripte wurden ausgefuehrt und Ollama wurde gestartet. Druecke eine Taste, um zu beenden.
pause
