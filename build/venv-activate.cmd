@echo off

cd %~dp0
call console-tools\title.cmd ACTIVATE VIRTUAL ENVIROMENT

call ..\.venv\scripts\activate.bat
IF ERRORLEVEL 1 EXIT /B 1