import requests

from configuration import SERVICE_URL
from src.baseclasses.response import Response
from src.schemas.post import POST_SCHEMA
from src.pydantic_schemas.post import Post


def test_getting_posts_validate_with_jsonschema():
    r = requests.get(url=SERVICE_URL)
    response = Response(r)

    response.assert_status_code(200).validate_schema_jsonchema(POST_SCHEMA)
    response.assert_number_of_elements(3)


def test_getting_posts_validate_with_pydantic():
    r = requests.get(url=SERVICE_URL)
    response = Response(r)

    response.assert_status_code(200).validate_schema_pydantic(Post)
