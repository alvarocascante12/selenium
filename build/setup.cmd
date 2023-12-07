@echo off

setlocal
pushd %~dp0

CALL .\console-tools\environment-variables.cmd
IF ERRORLEVEL 1 EXIT /B 1

CALL .\console-tools\title.cmd SETUP

CALL.\console-tools\setup-python-virtual-environment.cmd
CALL .\console-tools\selenium-setup.cmd

endlocal
popd
exit /b 0