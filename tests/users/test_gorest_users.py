from src.baseclasses.response import Response
from src.pydantic_schemas.user import User


def test_get_users_list(get_users, calculate):
    Response(get_users).assert_status_code(200).validate_schema_pydantic(User)
    # --> fixture that returned function
    print(calculate)
    print(calculate(1, 4))
    # <-- fixture that returned function

def test_number(make_number):
    assert 1 == 1
    print(make_number)