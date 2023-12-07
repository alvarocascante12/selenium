@echo off

setlocal
pushd %~dp0
call environment-variables.cmd
IF ERRORLEVEL 1 EXIT /B 1

call %PYTHON_VENV%\activate.bat
call title.cmd install dependency
call pip install selenium
call playwright-setup.cmd
call title.cmd done install selenium 

IF ERRORLEVEL 1 EXIT /B 1

call %PYTHON_VENV%\deactivate.bat


endlocal
popd
exit /b 0