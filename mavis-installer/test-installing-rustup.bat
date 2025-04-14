:: ====================================================================
:: Configuration and Logging
:: ====================================================================
set "USERNAME=%USERNAME%"
set "PYTHON_PATH=C:\Users\%USERNAME%\PycharmProjects\MAVIS\.env\Scripts\python.exe"
set "SCRIPT_INSTALL_RUSTUP=C:\Users\%USERNAME%\PycharmProjects\MAVIS\run\rust\install-rustup.py"
set "LOGFILE=%TEMP%\rustup_install_log.txt"

(
    echo ========================================================
    echo [INFO] Starting Rustup installation script
    echo [INFO] User: %USERNAME%
    echo [INFO] Start time: %date% %time%
    echo ========================================================
) >> "%LOGFILE%"

:: ====================================================================
:: Check if Rustup is already installed
:: ====================================================================
rustup --version >nul 2>&1
if %errorlevel% equ 0 (
    echo ✅ Rustup is already installed.
    echo [INFO] Rustup already installed >> "%LOGFILE%"
    goto End
)

echo Rustup is not installed.
echo [INFO] Rustup not found >> "%LOGFILE%"

:: ====================================================================
:: User prompt to confirm installation
:: ====================================================================
set /p install_rustup="Would you like to install Rustup? [y/n]: "
if /i not "%install_rustup%"=="y" (
    echo Installation canceled. Please install Rustup manually: https://rustup.rs/
    echo [WARN] User canceled the installation >> "%LOGFILE%"
    goto End
)

:: ====================================================================
:: Function: Download file using PowerShell
:: ====================================================================
:DownloadFile
:: Parameter %1 = URL, %2 = Output file path
echo [INFO] Attempting to download: %1 >> "%LOGFILE%"
powershell -Command ^
   "[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; " ^
   "Invoke-WebRequest -Uri '%~1' -OutFile '%~2'" 2>>"%LOGFILE%"
if exist "%~2" (
    echo [INFO] Download successful: %~2 >> "%LOGFILE%"
    exit /b 0
) else (
    echo [ERROR] Download failed: %~2 >> "%LOGFILE%"
    exit /b 2
)

:: ====================================================================
:: Attempt 1: Official installer from https://win.rustup.rs
:: ====================================================================
set "RUSTUP_URL=https://win.rustup.rs"
set "RUSTUP_INSTALLER=%TEMP%\rustup-init.exe"
echo [INFO] Attempt 1: Official installer >> "%LOGFILE%"
call :DownloadFile "%RUSTUP_URL%" "%RUSTUP_INSTALLER%"
if errorlevel 2 (
    echo [ERROR] Official download failed. Switching to alternative method.
    goto AlternativeDownload
)
echo [INFO] Running official installer >> "%LOGFILE%"
start /wait "%RUSTUP_INSTALLER%" -y
rustup --version >nul 2>&1
if %errorlevel% equ 0 (
    echo ✅ Rustup successfully installed using the official installer!
    echo [INFO] Installation successful in Attempt 1 >> "%LOGFILE%"
    goto Cleanup
) else (
    echo ❌ Error: Official installer did not work.
    echo [ERROR] Attempt 1: Installer error >> "%LOGFILE%"
)

:: ====================================================================
:: Attempt 2: Retry official installer
:: ====================================================================
echo [INFO] Attempt 2: Retrying official installer >> "%LOGFILE%"
if exist "%RUSTUP_INSTALLER%" (
    del "%RUSTUP_INSTALLER%" >nul 2>&1
)
call :DownloadFile "%RUSTUP_URL%" "%RUSTUP_INSTALLER%"
if errorlevel 2 (
    echo [ERROR] Retry download failed. Switching to alternative method.
    goto AlternativeDownload
)
start /wait "%RUSTUP_INSTALLER%" -y
rustup --version >nul 2>&1
if %errorlevel% equ 0 (
    echo ✅ Rustup successfully installed on the second attempt!
    echo [INFO] Installation successful in Attempt 2 >> "%LOGFILE%"
    goto Cleanup
) else (
    echo ❌ Error: Second attempt with official installer did not work.
    echo [ERROR] Attempt 2: Installer error >> "%LOGFILE%"
)

:: ====================================================================
:: Attempt 3: Alternative download method
:: ====================================================================
:AlternativeDownload
echo [INFO] Attempt 3: Alternative installer URL >> "%LOGFILE%"
set "RUSTUP_ALT_URL=https://static.rust-lang.org/rustup/dist/x86_64-pc-windows-msvc/rustup-init.exe"
set "RUSTUP_INSTALLER=%TEMP%\rustup-alt.exe"
call :DownloadFile "%RUSTUP_ALT_URL%" "%RUSTUP_INSTALLER%"
if errorlevel 2 (
    echo [ERROR] Alternative download failed.
    goto PythonFallback
)
echo [INFO] Running alternative installer >> "%LOGFILE%"
start /wait "%RUSTUP_INSTALLER%" -y
rustup --version >nul 2>&1
if %errorlevel% equ 0 (
    echo ✅ Rustup successfully installed using the alternative method!
    echo [INFO] Installation successful in Attempt 3 >> "%LOGFILE%"
    goto Cleanup
) else (
    echo ❌ Error: Alternative installation failed.
    echo [ERROR] Attempt 3: Alternative installer error >> "%LOGFILE%"
)

:: ====================================================================
:: Attempt 4: Fallback using Python installation script
:: ====================================================================
:PythonFallback
echo [INFO] Attempt 4: Python installation script fallback >> "%LOGFILE%"
if not exist "%SCRIPT_INSTALL_RUSTUP%" (
    echo ❌ Error: Python script not found: %SCRIPT_INSTALL_RUSTUP%
    echo [ERROR] Python script missing. >> "%LOGFILE%"
    echo Installation canceled. Please install Rustup manually: https://rustup.rs/
    goto End
)
echo [INFO] Running Python installation script >> "%LOGFILE%"
"%PYTHON_PATH%" "%SCRIPT_INSTALL_RUSTUP%"
rustup --version >nul 2>&1
if %errorlevel% equ 0 (
    echo ✅ Rustup successfully installed using the Python script!
    echo [INFO] Installation successful via Python script >> "%LOGFILE%"
    goto Cleanup
) else (
    echo ❌ Error: Python script installation attempt failed.
    echo [ERROR] Python script did not work >> "%LOGFILE%"
    echo Installation canceled. Please install Rustup manually: https://rustup.rs/
    goto End
)

:: ====================================================================
:: Cleanup temporary files
:: ====================================================================
:Cleanup
echo [INFO] Cleaning up temporary files... >> "%LOGFILE%"
if exist "%RUSTUP_INSTALLER%" (
    del "%RUSTUP_INSTALLER%" >nul 2>&1
    echo [INFO] Temporary file %RUSTUP_INSTALLER% removed >> "%LOGFILE%"
)
echo [INFO] Installation script completed. >> "%LOGFILE%"

:: ====================================================================
:: End of script
:: ====================================================================
:End
echo [INFO] End of installation script.
echo [INFO] Logfile: %LOGFILE%
