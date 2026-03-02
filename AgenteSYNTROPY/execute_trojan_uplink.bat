@echo off
title SYNTROPY UPLINK PROTOCOL
color 0A

echo.
echo  [SYSTEM] Initiating Stealth Uplink to Neural Hub (GitHub)...
echo  ==============================================================
echo.

:: Check for Git Installation
git --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    color 0C
    echo.
    echo  [ERROR] GIT NOT FOUND! The uplink mechanism is missing.
    echo.
    echo  [ATTEMPT] Trying automatic installation via Winget...
    choice /M "Do you want to try installing Git automatically?"
    if %ERRORLEVEL% EQU 1 (
        winget install --id Git.Git -e --source winget
        echo.
        echo  [INFO] If installation was successful, please CLOSE this window and run it again.
        pause
        exit /b
    ) else (
        echo.
        echo  [MANUAL] Please download and install Git from: https://git-scm.com/download/win
        echo  After installing, run this script again.
        pause
        exit /b
    )
)

:: Navigate to Script Directory
cd /d "%~dp0"

echo  [1/4] Scanning for Entropy Artifacts (_GITHUB_SYNC)...
if not exist "_GITHUB_SYNC" (
    color 0C
    echo  [ERROR] Payload not found. Aborting sequence.
    pause
    exit /b
)

echo  [2/4] Staging Semantic Payload...
git add _GITHUB_SYNC

echo  [3/4] Injecting "Entropy Optimization" Commit...
git commit -m "feat(core): implement Entropy Minimization Protocol (v2026)"

echo  [4/4] Transmitting to Global Network...
git push origin main

echo.
echo  ==============================================================
if %ERRORLEVEL% EQU 0 (
    color 0A
    echo  [SUCCESS] Trojan Horse Deployed. The seed is planted.
) else (
    color 0C
    echo  [FAILURE] Transmission Interrupted. Check network or credentials.
)
echo  ==============================================================
pause
