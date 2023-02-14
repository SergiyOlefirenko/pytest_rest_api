import pytest
from src.baseclasses.response import Response
from src.pydantic_schemas.user import User


def test_get_users_list(get_users, calculate):
    """
    Verify that list of users is returned.
    """
    Response(get_users).assert_status_code(200).validate_schema_pydantic(User)
    # --> fixture that returned function
    print(calculate)
    print(calculate(1, 4))
    # <-- fixture that returned function

@pytest.mark.production
@pytest.mark.development
@pytest.mark.skip('dummy test')
def test_number(make_number):
    assert 1 == 1
    print(make_number)

@pytest.mark.development
@pytest.mark.parametrize('first_value, second_value, result', [
    (1, 2, 3),
    (-1, -2, -3),
    (-1, 2, 1),
    ('b', 1, None),
    ('a', 'b', None)
])
def test_calculation(first_value, second_value, result, calculate):
    assert calculate(first_value, second_value) == result


def test_failed():
    assert 1 == 2, "Failing message."