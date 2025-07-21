import pytest
import allure
import json
from data.book_payloads import (
    valid_book,
    book_missing_description,
    book_with_long_title,
    book_empty_description_field,
    book_with_non_integer_pageCount
)
from utils.api_client import APIClient
from config.env_config import EXTERNAL_API_URL
external_api = APIClient(base_url=EXTERNAL_API_URL)


# ---- multiple payloads ----
@allure.epic("Book Management")
@allure.feature("Book Creation Validation")
@allure.story("US-1 System validates book payloads on POST")
@allure.description("POST /Books with various payloads")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("book_payload, expected_status", [
    pytest.param(valid_book(), 200, id="valid_book"),
    pytest.param(book_with_long_title(), 200, id="long_title"),
    pytest.param(book_missing_description(), 200, id="missing_desc"),
    pytest.param(book_empty_description_field(), 200, id="empty_description"),
    pytest.param(book_with_non_integer_pageCount(), 400, id="invalid_pageCount")
])
def test_post_book_various_payloads(book_payload, expected_status):
    with allure.step(f"POST /Books with payload expecting {expected_status}"):
        post_response = external_api.post("/Books", json=book_payload, expected_status=expected_status)
        allure.attach(
            json.dumps(book_payload, indent=2),
            name="Sent Payload",
            attachment_type=allure.attachment_type.JSON)
        allure.attach(post_response.text, name="Response", attachment_type=allure.attachment_type.JSON)
        assert post_response.status_code == expected_status, f"Unexpected response: {response.text}"

