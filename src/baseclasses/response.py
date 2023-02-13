from jsonschema import validate
from src.enums.global_enums import GlobalErrorMessages

class Response():

    def __init__(self, response) -> None:
        self.response = response
        self.response_status = response.status_code
        self.response_json = response.json()

    def validate_schema_jsonchema(self, schema):
        if isinstance(self.response_json, list):
            for item in self.response_json:
                validate(item, schema)
        else:
            validate(self.response_json, schema)

    def validate_schema_pydantic(self, schema):
        if isinstance(self.response_json, list):
            for item in self.response_json:
                schema.parse_obj(item)
        else:
            schema.parse_obj(self.response_json)

    def assert_status_code(self, status_code):
        if isinstance(status_code, list):
            assert self.response_status in status_code, GlobalErrorMessages.WRONG_STATUS_CODE.value
        else:
            assert self.response_status == status_code, GlobalErrorMessages.WRONG_STATUS_CODE.value
        return self

    def assert_number_of_elements(self, expected_number_of_elements):
        assert len(self.response_json) == expected_number_of_elements, GlobalErrorMessages.WRONG_ELEMENT_COUNT.value
        return self
