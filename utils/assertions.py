def assert_status_code(response, expected_status: int, context: str = "", payload=None):
    actual = response.status_code
    error_message = (
        f"[{context}] Expected status {expected_status}, got {actual}\n"
        f"Response body: {getattr(response, 'text', '')}"
    )
    if payload is not None:
        error_message += f"\nRequest payload: {payload}"
    if actual != expected_status:
        raise AssertionError(error_message)


def assert_has_field(obj: dict, field: str, context: str = ""):
    if field not in obj:
        raise AssertionError(
            f"[{context}] Missing expected field '{field}' in response: {obj}"
        )


def assert_equals(actual, expected, field: str, context: str = ""):
    if actual != expected:
        raise AssertionError(
            f"[{context}] Field '{field}': expected {expected}, got {actual}"
        )

def assert_valid_json(response, context: str = ""):
    try:
        return response.json()
    except Exception as e:
        raise AssertionError(
            f"[{context}] Invalid JSON in response.\n"
            f"Status: {getattr(response, 'status_code', None)}\n"
            f"Response text: {getattr(response, 'text', '')}"
        ) from e

def assert_response_by_schema(response_json, schema_model, context: str = ""):
    try:
        schema_model.model_validate(response_json)
    except Exception as e:
        raise AssertionError(
            f"[{context}] Response does not match schema {schema_model.__name__}: {e}\n"
            f"Response: {response_json}"
        ) from e