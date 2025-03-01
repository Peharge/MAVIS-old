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

echo.
echo Welcome to the MAVIS Installer 3
echo --------------------------------
echo Initiating high-tech installation...
echo Prepare for the next level! 🚀
echo.
echo MIT License
echo Copyright (c) 2024 Peharge
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
