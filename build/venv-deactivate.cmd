@echo off

cd %~dp0
call console-tools\title.cmd DEACTIVATE VIRTUAL ENVIROMENT

call ..\.venv\scripts\deactivate.bat
IF ERRORLEVEL 1 EXIT /B 1