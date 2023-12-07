@echo off


setlocal
pushd %~dp0

FOR %%A IN (%*) DO (
   FOR /f "tokens=1,2 delims=:" %%G IN ("%%A") DO set %%G=%%H
)


call .\console-tools\environment-variables.cmd
IF ERRORLEVEL 1 EXIT /B 1

call %PYTHON_VENV%\activate.bat
IF ERRORLEVEL 1 EXIT /B 1

call .\console-tools\subtitle.cmd Running tests

call .\console-tools\selenium-internal.cmd browser:chromium %*
IF ERRORLEVEL 1 EXIT /B 1
endlocal

popd

exit /b 0