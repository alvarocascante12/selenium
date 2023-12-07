# Selenium Automation Project

This automation project uses Selenium to perform automated testing on a web portal. Testing has been implemented at both the API and UI levels. Allure is used to generate detailed test reports.

## Project Structure

The project follows an organized structure to facilitate maintenance and expansion. The main structure is described below:
project_root/
|-- .venv/
|-- .results/
|-- automation/
| |-- selenium/
| |-- data-files/
| |-- new_post_data.json/
| |-- resources/
| |-- init.py
| |-- albums_api.py
| |-- comments_api.py
| |-- load_json.py
| |-- post_api.py
| |-- suite/
| |-- api/
| |-- init.py
| |-- test_albums_api.py
| |-- test_comments_api.py
| |-- test_posts_api.py
| |-- ui/
| |-- init.py
| |-- test_login.py
|-- build/
| |-- console-tools/
| |-- selenium-run.cmd
| |-- setup.cmd
| |-- test-run.cmd
| |-- venv-activate.cmd
| |-- venv-deactivate.cmd
|-- README.md

## Steps
- move to the build folder and run the setup.cmd file
`$ setup.cmd`
- Now you can run the tests
`$ test-run.cmd`

There is nothing more to say, just remember to have a version of python 3.xx on your local machine and a version of node

