@echo off

:: check if an argument is provided
if "%~1"=="" (
    echo Usage: logger.bat [filename]
    exit /b 1
)

:: append the time and data to log.txt
echo %TIME% %* >> log.txt