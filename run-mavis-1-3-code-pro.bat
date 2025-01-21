@echo off

set USERNAME=%USERNAME%
set PYTHON_PATH=C:\Users\%USERNAME%\PycharmProjects\MAVIS\.env\Scripts\python.exe
set SCRIPT_PATH_1=C:\Users\%USERNAME%\PycharmProjects\MAVIS\info\info-start-mavis-1-3-code-pro.py
set SCRIPT_PATH_2=C:\Users\%USERNAME%\PycharmProjects\MAVIS\install\install.py
set SCRIPT_PATH_update=C:\Users\%USERNAME%\PycharmProjects\MAVIS\update\update-repository-windows.py
set SCRIPT_PATH_3=C:\Users\%USERNAME%\PycharmProjects\MAVIS\install\install-mavis-1-3-code-pro.py
set SCRIPT_PATH_4=C:\Users\%USERNAME%\PycharmProjects\MAVIS\info\info.py
set PYTHON_SCRIPT_PATH=C:\Users\%USERNAME%\PycharmProjects\MAVIS\run_with_browser\run_with_browser.py
set SCRIPT_PATH_5=C:\Users\%USERNAME%\PycharmProjects\MAVIS\main\mavis-1-3-main-code-pro.py

if not exist "%PYTHON_PATH%" (
    echo Error: Python interpreter not found: %PYTHON_PATH%
    exit /B 1
)

if not exist "%SCRIPT_PATH_1%" (
    echo Error: Script not found: %SCRIPT_PATH_1%
    exit /B 1
)

"%PYTHON_PATH%" "%SCRIPT_PATH_1%"

if not exist "%SCRIPT_PATH_2%" (
    echo Error: Script not found: %SCRIPT_PATH_2%
    exit /B 1
)

"%PYTHON_PATH%" "%SCRIPT_PATH_2%"

if not exist "%SCRIPT_PATH_update%" (
    echo Error: Script not found: %SCRIPT_PATH_update%
    exit /B 1
)

"%PYTHON_PATH%" "%SCRIPT_PATH_update%"

if not exist "%SCRIPT_PATH_3%" (
    echo Error: Script not found: %SCRIPT_PATH_3%
    exit /B 1
)

"%PYTHON_PATH%" "%SCRIPT_PATH_3%"

if not exist "%SCRIPT_PATH_4%" (
    echo Error: Script not found: %SCRIPT_PATH_4%
    exit /B 1
)

"%PYTHON_PATH%" "%SCRIPT_PATH_4%"

if not exist "%PYTHON_SCRIPT_PATH%" (
    echo Error: Python script not found: %PYTHON_SCRIPT_PATH%
    exit /B 1
)

"%PYTHON_PATH%" "%PYTHON_SCRIPT_PATH%"

if not exist "%SCRIPT_PATH_5%" (
    echo Error: Script not found: %SCRIPT_PATH_5%
    exit /B 1
)

"%PYTHON_PATH%" "%SCRIPT_PATH_5%"

echo.
echo The scripts have been executed, Ollama has been started, and the browser has been opened.
echo Press any key to exit.
pause