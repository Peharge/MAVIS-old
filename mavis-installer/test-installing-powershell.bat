@echo off
setlocal EnableExtensions EnableDelayedExpansion

REM ============================================================
REM Secure batch script to install PowerShell 7
REM Installs PowerShell in C:\Users\%USERNAME%\PycharmProjects\MAVIS\
REM ============================================================

REM Set target path
set "INSTALL_DIR=C:\Users\%USERNAME%\PycharmProjects\MAVIS\PowerShell"
set "ZIP_FILE=C:\Users\%USERNAME%\PycharmProjects\MAVIS\PowerShell.zip"

REM Check if the installation directory exists
if exist "%INSTALL_DIR%" (
    echo ✅ PowerShell directory already exists: %INSTALL_DIR%
) else (
    echo ❌ PowerShell directory not found. Creating PowerShell directory...
    mkdir "%INSTALL_DIR%"
    if %ERRORLEVEL% NEQ 0 (
        echo ❌ Error creating PowerShell directory. Script will terminate.
        exit /b 1
    )
    echo ✅ PowerShell directory successfully created: %INSTALL_DIR%
)

REM Check if the ZIP file exists
if exist "%ZIP_FILE%" (
    echo ✅ PowerShell.zip found. Skipping download.
) else (
    echo ❌ PowerShell.zip not found. Starting download...

    REM Check processor architecture
    reg Query "HKLM\Hardware\Description\System\CentralProcessor\0" | find /i "x86" >nul && set OS=32BIT || set OS=64BIT

    REM Download the appropriate version of PowerShell
    if "%OS%"=="32BIT" (
        echo ❌ Downloading 32-bit version of PowerShell...
        c:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe -NoProfile -Command ^
        "[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; `
        $release = Invoke-RestMethod -Uri 'https://api.github.com/repos/PowerShell/PowerShell/releases/latest'; `
        $url = ($release.assets | Where-Object { $_.name -like '*win-x86.zip' }).browser_download_url; `
        Invoke-WebRequest -Uri $url -OutFile '%ZIP_FILE%'"
    )
    if "%OS%"=="64BIT" (
        echo ❌ Downloading 64-bit version of PowerShell...
        c:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe -NoProfile -Command ^
        "[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; `
        $release = Invoke-RestMethod -Uri 'https://api.github.com/repos/PowerShell/PowerShell/releases/latest'; `
        $url = ($release.assets | Where-Object { $_.name -like '*win-x64.zip' }).browser_download_url; `
        Invoke-WebRequest -Uri $url -OutFile '%ZIP_FILE%'"
    )
    if %ERRORLEVEL% NEQ 0 (
        echo ❌ Error downloading PowerShell.zip. Script will terminate.
        exit /b 1
    )
    echo ✅ PowerShell.zip successfully downloaded: %ZIP_FILE%
)

REM Check if PowerShell has already been extracted
if exist "%INSTALL_DIR%\pwsh.exe" (
    echo ✅ PowerShell already extracted: %INSTALL_DIR%
) else (
    echo ❌ Starting extraction of PowerShell.zip to %INSTALL_DIR%...

    REM Extract contents of PowerShell.zip
    c:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe -NoProfile -Command ^
    "[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; `
    Add-Type -AssemblyName System.IO.Compression.FileSystem; `
    [System.IO.Compression.ZipFile]::ExtractToDirectory('%ZIP_FILE%', '%INSTALL_DIR%')"
    if %ERRORLEVEL% NEQ 0 (
        echo ❌ Error extracting PowerShell.zip. Script will terminate.
        exit /b 1
    )
    echo ✅ PowerShell.zip successfully extracted to %INSTALL_DIR%.
)

REM Installation complete
echo ✅ PowerShell setup completed. Installed at: %INSTALL_DIR%
exit /b 0
