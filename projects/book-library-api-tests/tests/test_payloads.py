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
from utils.assertions import assert_status_code
from utils.endpoints import BOOKS_ENDP

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
    post_response = external_api.post(BOOKS_ENDP, json=book_payload, expected_status=expected_status)
    assert_status_code(post_response, expected_status, context=f"POST {BOOKS_ENDP}")

