@echo off

REM Englisch Peharge: This source code is released under the MIT License.
REM
REM Usage Rights:
REM The source code may be copied, modified, and adapted to individual requirements.
REM Users are permitted to use this code in their own projects, both for private and commercial purposes.
REM However, it is recommended to modify the code only if you have sufficient programming knowledge,
REM as changes could cause unintended errors or security risks.
REM
REM Dependencies and Additional Frameworks:
REM The code relies on the use of various frameworks and executes additional files.
REM Some of these files may automatically install further dependencies required for functionality.
REM It is strongly recommended to perform installation and configuration in an isolated environment
REM (e.g., a virtual environment) to avoid potential conflicts with existing software installations.
REM
REM Disclaimer:
REM Use of the code is entirely at your own risk.
REM Peharge assumes no liability for damages, data loss, system errors, or other issues
REM that may arise directly or indirectly from the use, modification, or redistribution of the code.
REM
REM Please read the full terms of the MIT License to familiarize yourself with your rights and obligations.

REM Deutsch Peharge: Dieser Quellcode wird unter der MIT-Lizenz veröffentlicht.
REM
REM Nutzungsrechte:
REM Der Quellcode darf kopiert, bearbeitet und an individuelle Anforderungen angepasst werden.
REM Nutzer sind berechtigt, diesen Code in eigenen Projekten zu verwenden, sowohl für private als auch kommerzielle Zwecke.
REM Es wird jedoch empfohlen, den Code nur dann anzupassen, wenn Sie über ausreichende Programmierkenntnisse verfügen,
REM da Änderungen unbeabsichtigte Fehler oder Sicherheitsrisiken verursachen könnten.
REM
REM Abhängigkeiten und zusätzliche Frameworks:
REM Der Code basiert auf der Nutzung verschiedener Frameworks und führt zusätzliche Dateien aus.
REM Einige dieser Dateien könnten automatisch weitere Abhängigkeiten installieren, die für die Funktionalität erforderlich sind.
REM Es wird dringend empfohlen, die Installation und Konfiguration in einer isolierten Umgebung (z. B. einer virtuellen Umgebung) durchzuführen,
REM um mögliche Konflikte mit bestehenden Softwareinstallationen zu vermeiden.
REM
REM Haftungsausschluss:
REM Die Nutzung des Codes erfolgt vollständig auf eigene Verantwortung.
REM Peharge übernimmt keinerlei Haftung für Schäden, Datenverluste, Systemfehler oder andere Probleme,
REM die direkt oder indirekt durch die Nutzung, Modifikation oder Weitergabe des Codes entstehen könnten.
REM
REM Bitte lesen Sie die vollständigen Lizenzbedingungen der MIT-Lizenz, um sich mit Ihren Rechten und Pflichten vertraut zu machen.

REM Français Peharge: Ce code source est publié sous la licence MIT.
REM
REM Droits d'utilisation:
REM Le code source peut être copié, édité et adapté aux besoins individuels.
REM Les utilisateurs sont autorisés à utiliser ce code dans leurs propres projets, à des fins privées et commerciales.
REM Il est cependant recommandé d'adapter le code uniquement si vous avez des connaissances suffisantes en programmation,
REM car les modifications pourraient provoquer des erreurs involontaires ou des risques de sécurité.
REM
REM Dépendances et frameworks supplémentaires:
REM Le code est basé sur l'utilisation de différents frameworks et exécute des fichiers supplémentaires.
REM Certains de ces fichiers peuvent installer automatiquement des dépendances supplémentaires requises pour la fonctionnalité.
REM Il est fortement recommandé d'effectuer l'installation et la configuration dans un environnement isolé (par exemple un environnement virtuel),
REM pour éviter d'éventuels conflits avec les installations de logiciels existantes.
REM
REM Clause de non-responsabilité:
REM L'utilisation du code est entièrement à vos propres risques.
REM Peharge n'assume aucune responsabilité pour tout dommage, perte de données, erreurs système ou autres problèmes,
REM pouvant découler directement ou indirectement de l'utilisation, de la modification ou de la diffusion du code.
REM
REM Veuillez lire l'intégralité des termes et conditions de la licence MIT pour vous familiariser avec vos droits et responsabilités.

setlocal enabledelayedexpansion

chcp 65001

echo -------------------------------------------------
echo        Welcome to the MAVIS Launcher 4
echo -------------------------------------------------
echo      Initiating high-tech installation...
echo           Prepare for the next level!
echo.
echo                  MIT License
echo              Copyright (c) 2024
echo                    Peharge
echo.
echo Permission is hereby granted, free of charge, to any person obtaining a copy
echo of this software and associated documentation files (the "Software"), to deal
echo in the Software without restriction, including without limitation the rights
echo to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
echo copies of the Software, and to permit persons to whom the Software is
echo furnished to do so, subject to the following conditions:
echo.
echo The above copyright notice and this permission notice shall be included in all
echo copies or substantial portions of the Software.
echo.
echo THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
echo IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
echo FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
echo AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
echo LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
echo OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
echo SOFTWARE.
echo.
echo Gooo...
echo.

:: Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python 3.12 is not installed.
    set /p install_python="Would you like to install Python 3.12? [y/n]:"

    if /i "%install_python%"=="y" (
        echo Downloading and installing Python 3.12...

        :: Define Python installer URL and download path
        set "PYTHON_URL=https://www.python.org/ftp/python/3.12.2/python-3.12.2-amd64.exe"
        set "PYTHON_INSTALLER=%TEMP%\python-3.12.2-installer.exe"

        :: Securely download Python using PowerShell
        powershell -Command "& {
            [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12;
            Invoke-WebRequest -Uri '%PYTHON_URL%' -OutFile '%PYTHON_INSTALLER%'
        }"

        :: Verify if the installer was downloaded
        if exist "%PYTHON_INSTALLER%" (
            echo Running the Python installer...

            :: Install Python silently for all users and add to PATH
            start /wait %PYTHON_INSTALLER% /quiet InstallAllUsers=1 PrependPath=1 Include_test=0

            :: Verify installation
            python --version >nul 2>&1
            if %errorlevel% neq 0 (
                echo ❌ Error: Python installation failed!
            ) else (
                echo ✅ Python 3.12 was successfully installed!
            )
        ) else (
            echo ❌ Error: Python installer could not be downloaded!
        )
    ) else (
        echo Installation aborted. Please install Python 3.12 manually from: https://www.python.org/downloads
    )
) else (
    echo ✅ Python is already installed.
)

:: Check if Git is installed
git --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Git is not installed.
    set /p install_git="Would you like to install Git? [y/n]:"

    if /i "%install_git%"=="y" (
        echo Downloading and installing Git...

        :: Define Git installer URL and download path
        set "GIT_URL=https://github.com/git-for-windows/git/releases/latest/download/Git-2.44.0-64-bit.exe"
        set "GIT_INSTALLER=%TEMP%\git-installer.exe"

        :: Securely download Git using PowerShell
        powershell -Command "& {
            [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12;
            Invoke-WebRequest -Uri '%GIT_URL%' -OutFile '%GIT_INSTALLER%'
        }"

        :: Verify if the installer was downloaded
        if exist "%GIT_INSTALLER%" (
            echo Running the Git installer...

            :: Install Git silently with default options
            start /wait %GIT_INSTALLER% /VERYSILENT /NORESTART /CLOSEAPPLICATIONS

            :: Verify installation
            git --version >nul 2>&1
            if %errorlevel% neq 0 (
                echo ❌ Error: Git installation failed!
            ) else (
                echo ✅ Git was successfully installed!
            )
        ) else (
            echo ❌ Error: Git installer could not be downloaded!
        )
    ) else (
        echo Installation aborted. Please install Git manually from: https://git-scm.com/downloads
    )
) else (
    echo ✅ Git is already installed.
)

:: Check if Ollama is installed
ollama --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Ollama is not installed.
    set /p install_ollama="Would you like to install Ollama? [y/n]:"

    if /i "%install_ollama%"=="y" (
        echo Downloading and installing Ollama...

        :: Define Ollama installer URL and download path
        set "OLLAMA_URL=https://ollama.com/download/OllamaSetup.exe"
        set "OLLAMA_INSTALLER=%TEMP%\OllamaSetup.exe"

        :: Securely download Ollama using PowerShell
        powershell -Command "& {
            [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12;
            Invoke-WebRequest -Uri '%OLLAMA_URL%' -OutFile '%OLLAMA_INSTALLER%'
        }"

        :: Verify if the installer was downloaded
        if exist "%OLLAMA_INSTALLER%" (
            echo Running the Ollama installer...

            :: Install Ollama silently
            start /wait %OLLAMA_INSTALLER% /silent /norestart

            :: Verify installation
            ollama --version >nul 2>&1
            if %errorlevel% neq 0 (
                echo ❌ Error: Ollama installation failed!
            ) else (
                echo ✅ Ollama was successfully installed!
            )
        ) else (
            echo ❌ Error: Ollama installer could not be downloaded!
        )
    ) else (
        echo Installation aborted. Please install Ollama manually from: https://ollama.com/download
    )
) else (
    echo ✅ Ollama is already installed.
)

:: Check if FFmpeg is installed
ffmpeg -version >nul 2>&1
if %errorlevel% neq 0 (
    echo FFmpeg is not installed.
    set /p install_ffmpeg="Would you like to install FFmpeg? [y/n]:"

    if /i "%install_ffmpeg%"=="y" (
        echo Downloading and installing FFmpeg...

        :: Define FFmpeg installer URL and download path
        set "FFMPEG_URL=https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip"
        set "FFMPEG_ZIP=%TEMP%\ffmpeg.zip"
        set "FFMPEG_EXTRACT=%TEMP%\ffmpeg"

        :: Securely download FFmpeg using PowerShell
        powershell -Command "& {
            [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12;
            Invoke-WebRequest -Uri '%FFMPEG_URL%' -OutFile '%FFMPEG_ZIP%'
        }"

        :: Verify if the zip file was downloaded
        if exist "%FFMPEG_ZIP%" (
            echo Extracting FFmpeg...

            :: Extract FFmpeg (requires PowerShell 5+)
            powershell -Command "Expand-Archive -Path '%FFMPEG_ZIP%' -DestinationPath '%FFMPEG_EXTRACT%' -Force"

            :: Move FFmpeg to C:\ffmpeg (system-wide installation)
            if not exist "C:\ffmpeg" mkdir "C:\ffmpeg"
            xcopy "%FFMPEG_EXTRACT%\ffmpeg-*\" "C:\ffmpeg\" /E /Y >nul

            :: Add FFmpeg to System PATH
            setx PATH "C:\ffmpeg\bin;%PATH%" /M

            :: Verify installation
            ffmpeg -version >nul 2>&1
            if %errorlevel% neq 0 (
                echo ❌ Error: FFmpeg installation failed!
            ) else (
                echo ✅ FFmpeg was successfully installed and added to PATH!
            )
        ) else (
            echo ❌ Error: FFmpeg could not be downloaded!
        )
    ) else (
        echo Installation aborted. Please install FFmpeg manually from: https://ffmpeg.org/download.html#build-windows
    )
) else (
    echo ✅ FFmpeg is already installed.
)

:: Check if Rustup is installed
rustup --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Rustup is not installed.
    set /p install_rustup="Would you like to install Rustup? [y/n]:"

    if /i "%install_rustup%"=="y" (
        echo Downloading and installing Rustup...

        :: Define Rustup installer URL and download path
        set "RUSTUP_URL=https://win.rustup.rs"
        set "RUSTUP_INSTALLER=%TEMP%\rustup-init.exe"

        :: Securely download Rustup using PowerShell
        powershell -Command "& {
            [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12;
            Invoke-WebRequest -Uri '%RUSTUP_URL%' -OutFile '%RUSTUP_INSTALLER%'
        }"

        :: Verify if the installer was downloaded
        if exist "%RUSTUP_INSTALLER%" (
            echo Running the Rustup installer...

            :: Install Rustup silently
            start /wait %RUSTUP_INSTALLER% -y

            :: Verify installation
            rustup --version >nul 2>&1
            if %errorlevel% neq 0 (
                echo ❌ Error: Rustup installation failed!
            ) else (
                echo ✅ Rustup was successfully installed!
            )
        ) else (
            echo ❌ Error: Rustup installer could not be downloaded!
        )
    ) else (
        echo Installation aborted. Please install Rustup manually from: https://sh.rustup.rs
    )
) else (
    echo ✅ Rustup is already installed.
)

:: Define project path
set "PYCHARM_PROJECTS=%USERPROFILE%\PycharmProjects"
set "MAVIS_DIR=%PYCHARM_PROJECTS%\MAVIS"

:: Function to double-check whether Git is installed and working
where git >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Git is not installed or not in PATH. Installing Git first...

    :: Set Git download URL and installer path
    set "GIT_URL=https://github.com/git-for-windows/git/releases/latest/download/Git-2.44.0-64-bit.exe"
    set "GIT_INSTALLER=%TEMP%\git-installer.exe"

    :: Check if Internet is available before download
    ping -n 1 google.com >nul 2>&1
    if %errorlevel% neq 0 (
        echo ❌ No internet connection! Please connect to the internet and try again.
        exit /b 1
    )

    :: Securely download Git installer using PowerShell
    powershell -Command "& {
        [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12;
        Invoke-WebRequest -Uri '%GIT_URL%' -OutFile '%GIT_INSTALLER%'
    }"

    :: Verify if Git installer was downloaded successfully
    if not exist "%GIT_INSTALLER%" (
        echo ❌ Error: Could not download Git installer! Check your internet connection or download it manually from:
        echo    https://git-scm.com/downloads
        exit /b 1
    )

    :: Install Git silently
    echo Installing Git silently...
    start /wait %GIT_INSTALLER% /VERYSILENT /NORESTART /CLOSEAPPLICATIONS

    :: Verify installation
    where git >nul 2>&1
    if %errorlevel% neq 0 (
        echo ❌ Git installation failed! Please install it manually from:
        echo    https://git-scm.com/downloads
        exit /b 1
    ) else (
        echo ✅ Git was successfully installed and configured!
    )
)

:: Ensure PyCharm Projects directory exists
if not exist "%PYCHARM_PROJECTS%" (
    echo Creating project directory: %PYCHARM_PROJECTS%...
    mkdir "%PYCHARM_PROJECTS%"
)

:: Change to PyCharm Projects directory
cd /d "%PYCHARM_PROJECTS%"

:: Check if MAVIS folder exists
if not exist "%MAVIS_DIR%" (
    echo Cloning MAVIS repository from GitHub...

    :: Check if GitHub is reachable
    ping -n 1 github.com >nul 2>&1
    if %errorlevel% neq 0 (
        echo ❌ Error: Cannot reach GitHub! Check your internet connection and firewall settings.
        exit /b 1
    )

    git clone https://github.com/Peharge/MAVIS.git "%MAVIS_DIR%"

    if %errorlevel% neq 0 (
        echo ❌ Error: Cloning MAVIS repository failed! Make sure GitHub is accessible and the URL is correct.
        exit /b 1
    ) else (
        echo ✅ MAVIS repository cloned successfully!
    )
) else (
    echo MAVIS repository already exists. Checking for updates...
    cd /d "%MAVIS_DIR%"

    git pull
    if %errorlevel% neq 0 (
        echo ❌ Error: Could not update MAVIS repository! Check your internet connection or Git configuration.
        exit /b 1
    ) else (
        echo ✅ MAVIS repository is up-to-date!
    )
)

:: Define MAVIS project path
set "PYCHARM_PROJECTS=%USERPROFILE%\PycharmProjects"
set "MAVIS_DIR=%PYCHARM_PROJECTS%\MAVIS"
set "MAVIS_ENV_FILE=%MAVIS_DIR%\.env"
set "MAVIS_RUN_FILE=%MAVIS_DIR%\run-mavis-4-all.bat"

:: Ensure MAVIS directory exists
if not exist "%MAVIS_DIR%" (
    echo ❌ Error: MAVIS directory does not exist!
    echo Make sure the repository was cloned correctly.
    exit /b 1
)

:: Change to MAVIS directory
cd /d "%MAVIS_DIR%" || (
    echo ❌ Error: Failed to access MAVIS directory!
    exit /b 1
)

:: Ensure .env file exists and is correctly configured
if not exist "%MAVIS_ENV_FILE%" (
    echo Creating .env file...
    (
        echo # Environment variables for MAVIS
        echo PYTHONPATH=%MAVIS_DIR%
    ) > "%MAVIS_ENV_FILE%"

    if %errorlevel% neq 0 (
        echo ❌ Error: Could not create .env file!
        exit /b 1
    ) else (
        echo ✅ .env file created successfully!
    )
) else (
    echo ✅ .env file already exists.
)

:: Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Error: Python is not installed or not found in PATH!
    echo Please install Python 3.12 and make sure it is in your system PATH.
    exit /b 1
)

:: Check if MAVIS run file exists
if not exist "%MAVIS_RUN_FILE%" (
    echo ❌ Error: run-mavis-4-all.bat not found!
    echo Please verify that the file exists in: %MAVIS_DIR%
    exit /b 1
)

:: Execute run-mavis-4-all.bat
echo ✅ Starting MAVIS...
call "%MAVIS_RUN_FILE%"

:: Verify if execution was successful
if %errorlevel% neq 0 (
    echo ❌ Error: MAVIS did not start successfully!
    exit /b 1
) else (
    echo ✅ MAVIS started successfully!
)

:: Completion
echo 🎉 All tasks have been completed successfully!
echo.

pause
exit /b
