@echo off
setlocal enabledelayedexpansion

:: Funktionen für die Installation
:install_git
where git >nul 2>nul
if %errorlevel%==0 (
    echo ✅ Git is already installed.
) else (
    echo 🔄 Installing Git...
    winget install --id Git.Git -e --source winget || (
        echo ❌ Git installation failed. Visit https://git-scm.com.
        exit /b 1
    )
)

:install_python
where python >nul 2>nul
if %errorlevel%==0 (
    echo ✅ Python is already installed.
) else (
    echo 🔄 Installing Python...
    winget install --id Python.Python.3 -e --source winget || (
        echo ❌ Python installation failed. Visit https://www.python.org.
        exit /b 1
    )
)

:install_ollama
where ollama >nul 2>nul
if %errorlevel%==0 (
    echo ✅ Ollama is already installed.
) else (
    echo 🔄 Installing Ollama...
    start https://ollama.com/download || (
        echo ❌ Ollama installation failed. Visit https://ollama.com/download.
        exit /b 1
    )
)

:create_folder
set folder=%USERPROFILE%\PycharmProjects
if not exist "%folder%" (
    mkdir "%folder%"
    echo ✅ Folder created: %folder%
) else (
    echo ℹ️ Folder already exists: %folder%
)

:clone_repository
set repo_url=https://github.com/Peharge/MAVIS
set target_path=%USERPROFILE%\PycharmProjects\MAVIS
if exist "%target_path%" (
    echo ℹ️ Repository has already been cloned.
) else (
    echo 🔄 Cloning repository...
    git clone %repo_url% %target_path% || (
        echo ❌ Repository could not be cloned.
        exit /b 1
    )
)

:create_virtual_environment
set env_path=%USERPROFILE%\PycharmProjects\MAVIS\env
if exist "%env_path%" (
    echo ℹ️ Virtual environment already exists.
) else (
    echo 🔄 Creating virtual environment...
    python -m venv "%env_path%" || (
        echo ❌ Virtual environment could not be created.
        exit /b 1
    )
)

:start_ui
set script_path=%USERPROFILE%\PycharmProjects\MAVIS\run-mavis-all.bat
if exist "%script_path%" (
    echo 🚀 Starting User Interface...
    call "%script_path%"
) else (
    echo ❌ User interface script not found.
    exit /b 1
)

:menu
cls
echo MAVIS Installer
echo =================
echo 1. Install prerequisites (Git, Python, Ollama)
echo 2. Create folder
echo 3. Clone repository
echo 4. Create virtual environment
echo 5. Start user interface
echo 6. Finish
echo =================
set /p choice=Select an option:
if "%choice%"=="1" call :install_git & call :install_python & call :install_ollama
if "%choice%"=="2" call :create_folder
if "%choice%"=="3" call :clone_repository
if "%choice%"=="4" call :create_virtual_environment
if "%choice%"=="5" call :start_ui
if "%choice%"=="6" exit /b 0
goto menu
