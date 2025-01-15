@echo off

set USERNAME=%USERNAME%
set PYTHON_PATH=C:\Users\%USERNAME%\PycharmProjects\MAVIS\.env\Scripts\python.exe
set SCRIPT_PATH_1=C:\Users\%USERNAME%\PycharmProjects\MAVIS\info.py
set SCRIPT_PATH_2=C:\Users\%USERNAME%\PycharmProjects\MAVIS\mavis-1-2-main-main.py
set PYTHON_SCRIPT_PATH=C:\Users\%USERNAME%\PycharmProjects\MAVIS\run_with_browser.py

:: Überprüfen, ob der Python-Interpreter existiert
if not exist "%PYTHON_PATH%" (
    echo Fehler: Python-Interpreter nicht gefunden: %PYTHON_PATH%
    exit /B 1
)

:: Überprüfen, ob das erste Python-Skript existiert
if not exist "%SCRIPT_PATH_1%" (
    echo Fehler: Skript nicht gefunden: %SCRIPT_PATH_1%
    exit /B 1
)

"%PYTHON_PATH%" "%SCRIPT_PATH_1%"

:: Überprüfen, ob das zweite Python-Skript existiert
if not exist "%SCRIPT_PATH_2%" (
    echo Fehler: Skript nicht gefunden: %SCRIPT_PATH_2%
    exit /B 1
)

"%PYTHON_PATH%" "%SCRIPT_PATH_2%"

:: Überprüfen, ob das Python-Skript existiert
if not exist "%PYTHON_SCRIPT_PATH%" (
    echo Fehler: Python-Skript nicht gefunden: %PYTHON_SCRIPT_PATH%
    exit /B 1
)

:: Starte das Python-Skript, das Ollama startet und den Browser öffnet
"%PYTHON_PATH%" "%PYTHON_SCRIPT_PATH%"

echo.
echo Die Skripte wurden ausgefuehrt, Ollama wurde gestartet und der Browser wurde geöffnet.
echo Druecke eine Taste, um zu beenden.
pause