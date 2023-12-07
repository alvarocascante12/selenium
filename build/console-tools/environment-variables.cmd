pushd %~dp0
call subtitle.cmd Up Enviroment Variables
pushd ..\
SET bUILD_FOLDER_FULL_PATH=%CD%
pushd ..\
set PROJECT_ROOT=%CD%
pushd ..\
popd
popd
popd
set BUILD_RESULTS_FOLDER=%PROJECT_ROOT%\results
set PYTHONPATH=%PYTHONPATH%

if not exist %BUILD_RESULTS_FOLDER% md %BUILD_RESULTS_FOLDER% 
SET TEST_RESULTS_FOLDER=%BUILD_RESULTS_FOLDER%\selenium-results


SET PYTHON_VENV=%PROJECT_ROOT%\.venv\scripts
SET TEST_RESULTS_PATH=%BUILD_RESULTS_FOLDER%\selenium-results\
SET sele_TEST_PATH=%PROJECT_ROOT:\=/%/automation/selenium
if not exist %TEST_RESULTS_PATH% md %TEST_RESULTS_PATH%
SET TESTS_PATH=%PROJECT_ROOT:\=/%/automation/selenium/suite
SET PLAYWRIGHT_BROWSERS_PATH=%USERPROFILE%\pw-browsers

popd