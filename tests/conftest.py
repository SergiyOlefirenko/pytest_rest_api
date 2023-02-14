import pytest
from random import randrange


# this fixture will be accessible from both tests folders ('users' and 'something')
@pytest.fixture
def get_number():
    return randrange(1, 1000, 5)


# --> function and that will be returned by fixture
def _calculate(a, b):
    return a + b

@pytest.fixture
def calculate():
    return _calculate
# <-- function and that will be returned by fixture


# setup and teardown fixtures
@pytest.fixture
def make_number():
    print("\nI'm getting number.")
    number = randrange(1, 1000, 5)
    yield number
    print(f"\nNumber at home {number}")