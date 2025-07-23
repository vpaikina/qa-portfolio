import allure
import pytest

from config.env_config import EXTERNAL_API_URL
from steps.book_steps import get_book_by_id, create_book, assert_book_contract
from utils.api_client import APIClient
from utils.endpoints import BOOKS_ENDP

external_api = APIClient(base_url=EXTERNAL_API_URL)


# ---- contract validation----
@allure.epic("Book API Contracts")
@allure.feature("Book Schema Validation")
@allure.story("US-3 GET /books/{id} returns valid Book model")
@allure.description("Contract test: validate Book model structure in API response.")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.contract
@pytest.mark.smoke
def test_book_response_contract(api_client, existing_valid_book):
    book = existing_valid_book
    get_resp = get_book_by_id(api_client, book.id)
    with allure.step("Validate book structure against Pydantic schema"):
        assert_book_contract(get_resp, f"GET {BOOKS_ENDP}/{book.id}")


@allure.epic("Book API Contracts")
@allure.feature("Book Schema Validation")
@allure.story("US-4: Contract enforcement for book creation")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description(
    """
This test intentionally sends an invalid book structure - empty json payload
It should fail with HTTP 400 (Bad Request)
but the system currently creates a book with null/zero fields
"""
)
@pytest.mark.xfail(
    reason="Known issue: backend accepts empty book payload (should be 400)."
)
@allure.severity(allure.severity_level.CRITICAL)
@allure.link(
    "https://github.com/vpaikina/qa-portfolio/blob/main/assets/sample-bug-report.md",
    name="Bug: [API_Contract] API allows POST /books with empty body (expected 400, got 200)",
)
@pytest.mark.contract
def test_post_empty_book_rejected():
    invalid_book = {}
    create_book(external_api, invalid_book, expected_status=400)
