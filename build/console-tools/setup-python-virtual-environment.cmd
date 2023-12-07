@echo off

setlocal
pushd %~dp0
call environment-variables.cmd
IF ERRORLEVEL 1 EXIT /B 1

set PROJECT_TYPE=%1
if [%PROJECT_TYPE%]==[] set PROJECT_TYPE=robot

call subtitle.cmd Setting up Python Virtual Environment

pushd %PROJECT_ROOT%
call python -m venv .venv
IF ERRORLEVEL 1 EXIT /B 1
call %PYTHON_VENV%\python -m pip install --upgrade pip
IF ERRORLEVEL 1 EXIT /B 1
popd

if not exist %BUILD_FOLDER_FULL_PATH%\requirements.txt call error.cmd "Missing %BUILD_FOLDER_FULL_PATH%\requirements.txt file"
popd
endlocal

exit /b 0