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
        return self

    def validate_schema_pydantic(self, schema, parent=None):
        json_value = self.response_json.get(parent) if parent else self.response_json
        if isinstance(json_value, list):
            for item in json_value:
                schema.parse_obj(item)
        else:
            schema.parse_obj(json_value)
        return self

    def assert_status_code(self, status_code):
        if isinstance(status_code, list):
            assert self.response_status in status_code, GlobalErrorMessages.WRONG_STATUS_CODE.value
        else:
            assert self.response_status == status_code, GlobalErrorMessages.WRONG_STATUS_CODE.value
        return self

    def assert_number_of_elements(self, expected_number_of_elements):
        assert len(self.response_json) == expected_number_of_elements, GlobalErrorMessages.WRONG_ELEMENT_COUNT.value
        return self

    def __str__(self):
        return \
            f"\nStatus code: {self.response_status}\n" \
            f"Requested url: {self.response.url}\n" \
            f"Response body: {self.response_json}"
