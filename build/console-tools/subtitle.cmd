setlocal
pushd %~dp0
set SUBTITLE=%*
echo _________________________________________________________________-
echo ^>^>^> %TIME%; %SUBTITLE% 
echo.%COLOR_RESET%

popd
endlocal