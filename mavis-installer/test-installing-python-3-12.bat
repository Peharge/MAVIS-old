@echo off
setlocal EnableDelayedExpansion

:: Define variables
set PYTHON_VERSION=3.12.10
set PYTHON_EXECUTABLE=py -3.12
set PYTHON_INSTALLER_PATH=%USERPROFILE%\Downloads
set INSTALLER_NAME=python-!PYTHON_VERSION!-amd64.exe
set INSTALLER_URL=https://www.python.org/ftp/python/!PYTHON_VERSION!/!INSTALLER_NAME!
set LOG_DIR=%USERPROFILE%\Desktop\Python_Install_Logs
set LOG_FILE=!LOG_DIR!\python_install_!PYTHON_VERSION!.log

:: Icons for feedback
set CHECK_MARK=✅
set CROSS_MARK=❌

:: Check if Python 3.12 is already installed
%PYTHON_EXECUTABLE% -c "import sys; version = sys.version.split()[0]; assert version.startswith('%PYTHON_VERSION%')" >nul 2>&1
if not errorlevel 1 (
    echo !CHECK_MARK! Python !PYTHON_VERSION! is already installed on your system.
    pause
    goto end
)

:: Prompt the user to install Python
:prompt_user
set /p USER_INPUT=Do you want to install Python !PYTHON_VERSION!? [y/n]:
if /i "!USER_INPUT!"=="Y" goto proceed_installation
if /i "!USER_INPUT!"=="N" goto end
echo Invalid input. Please type Y or N.
goto prompt_user

:: Proceed with installation
:proceed_installation

:: Ensure the log directory exists
if not exist "!LOG_DIR!" (
    echo Creating log directory...
    mkdir "!LOG_DIR!"
    if errorlevel 1 (
        echo !CROSS_MARK! Failed to create log directory at !LOG_DIR!. Check permissions.
        pause
        goto end
    )
)

:: Output to console and log file
echo %DATE% %TIME%: Starting download of Python !PYTHON_VERSION! >> "!LOG_FILE!"
echo Starting download of Python !PYTHON_VERSION!...

:: Download Python installer using PowerShell
powershell -Command "Invoke-WebRequest -Uri '!INSTALLER_URL!' -OutFile '!PYTHON_INSTALLER_PATH!\!INSTALLER_NAME!'" >> "!LOG_FILE!" 2>&1
if errorlevel 1 (
    echo !CROSS_MARK! Download failed, see log at !LOG_FILE! for details.
    pause
    goto end
)

:: Start installation
echo %DATE% %TIME%: Starting installation of Python !PYTHON_VERSION! >> "!LOG_FILE!"
echo Starting installation of Python !PYTHON_VERSION!...

"!PYTHON_INSTALLER_PATH!\!INSTALLER_NAME!" /passive InstallAllUsers=1 PrependPath=1 Include_test=0 >> "!LOG_FILE!" 2>&1
if errorlevel 1 (
    echo !CROSS_MARK! Installation failed, see log at !LOG_FILE! for details.
    pause
    goto end
)

:: Verify Python installation
echo Verifying Python installation...
%PYTHON_EXECUTABLE% -c "import sys; print('Python version:', sys.version)" >> "!LOG_FILE!" 2>&1
if errorlevel 1 (
    echo !CROSS_MARK! Verification failed. Python !PYTHON_VERSION! might not have installed correctly.
    pause
    goto end
)

:: Cleaning up installation files
echo Cleaning up installation files...
del /f /q "!PYTHON_INSTALLER_PATH!\!INSTALLER_NAME!" >> "!LOG_FILE!" 2>&1

:: Final message
echo !CHECK_MARK! Python !PYTHON_VERSION! installation and verification completed successfully.
echo %DATE% %TIME%: Python !PYTHON_VERSION! installation and verification completed successfully. >> "!LOG_FILE!"
echo Installation complete. Press any key to exit.
pause

:end
endlocal