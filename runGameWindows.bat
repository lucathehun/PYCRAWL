@echo off
REM Find the directory the script is in
SET "DIR=%~dp0"
REM Change to the directory where the script is located
cd /d "%DIR%"
REM Run the Python script
python "startGame.py"

