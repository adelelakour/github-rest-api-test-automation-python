import jsonschema
from src.users.schema import USER_SCHEMA, ERROR_SCHEMA


def validate_valid_user(response_body):
    jsonschema.validate(instance=response_body, schema=USER_SCHEMA)

def validate_invalid_user(response_body):
    jsonschema.validate(instance=response_body, schema=ERROR_SCHEMA)
