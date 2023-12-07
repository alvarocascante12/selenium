@echo off

setlocal
pushd %~dp0

CALL .\console-tools\environment-variables.cmd
IF ERRORLEVEL 1 EXIT /B 1

CALL .\console-tools\title.cmd RUN TEST
set PYTHONPATH=%PROJECT_ROOT%\automation\selenium\resource;%PYTHONPATH%

CALL selenium-run.cmd %*

endlocal
popd
exit /b 0