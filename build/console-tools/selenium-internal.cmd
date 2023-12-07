@echo off

setlocal
pushd %~dp0

call pytest %TESTS_PATH%\api\ --alluredir=./%TEST_RESULTS_FOLDER%
@REM call pytest %TESTS_PATH%\ui\ --alluredir=./%TEST_RESULTS_FOLDER%

@REM If you want to see the results in html, uncomment this line you must have the java jdk on your machine to be able to set up the allure server
@REM allure serve ./%TEST_RESULTS_FOLDER%

endlocal
popd
exit /b 0