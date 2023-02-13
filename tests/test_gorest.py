import requests
from configuration import GOREST_URL
from src.baseclasses.response import Response
from src.pydantic_schemas.user import User

resp = requests.get(GOREST_URL).json()
print(resp)


def test_get_users_list():
    test_object = Response(requests.get(GOREST_URL))
    test_object.assert_status_code(300).validate_schema_pydantic(User)