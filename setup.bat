@echo off
setlocal

echo Checking if virtualenv is installed...
timeout /t 1 >nul
cls

python -m pip show virtualenv >nul 2>&1
if errorlevel 1 (
    echo Installing virtualenv...
    python -m pip install virtualenv
) else (
    echo virtualenv is already installed
)
timeout /t 1 >nul
cls

echo Creating '.venv' virtual environment...
python -m virtualenv .venv
timeout /t 1 >nul
cls

echo Activating virtual environment...
call .venv\Scripts\activate.bat
timeout /t 1 >nul
cls

echo Installing required packages...
pip install pyyaml keyboard mido python-rtmidi textual
timeout /t 1 >nul
cls

echo Setup complete!
pause
