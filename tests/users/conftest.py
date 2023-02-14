import pytest
import requests
from configuration import GOREST_URL


# this fixture can be accessible only from 'users' folder
@pytest.fixture
def get_users():
    return requests.get(GOREST_URL)
