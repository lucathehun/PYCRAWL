@echo off
REM Find the directory the script is in
SET "DIR=%~dp0"
REM Run the Python script using its relative path
python "%DIR%startGame.py"

