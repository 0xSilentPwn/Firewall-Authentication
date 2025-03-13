@echo off
:: Check for Admin Privileges
NET SESSION >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    powershell -Command "Start-Process cmd -ArgumentList '/c %~s0' -Verb RunAs"
    exit
)

:: Change directory to where your Python script is located
cd /d C:\Path\To\Your\Project\Folder

:: Run the Python script
start "" python auth_server.py
