@echo off

set PYTHON_PATH=C:\Users\julia\PycharmProjects\MAVIS\.env\Scripts\python.exe
set SCRIPT_PATH_1=C:\Users\julia\PycharmProjects\MAVIS\info.py
set SCRIPT_PATH_2=C:\Users\julia\PycharmProjects\MAVIS\main.py

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

echo.
echo Die Skripte wurden ausgefuehrt. Druecke eine Taste, um zu beenden.
pause
