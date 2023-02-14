# Pytest REST API examples


To run test from command line create in the root folder '.env' file with the following content:

> `PYTHONPATH=${PYTHONPATH}:${PWD}`


To generate allure reports execute the following commands:

1. Run tests with '--alluredir=allureress' parameter

    > pytest -v -s tests/users/test_gorest_users.py --alluredir=allureress

2. Start allure reports server:

    > allure serve allureress