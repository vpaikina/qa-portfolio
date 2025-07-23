import pytest
from utils.api_client import APIClient
from data.book_payloads import valid_book
from schemas.book import BookResponseModel
from utils.resource_tracker import tracked_client


@pytest.fixture(scope="function")
def api_client() -> APIClient:
    return APIClient()


@pytest.fixture
def existing_valid_book(api_client):
    with tracked_client(api_client) as (client, tracker):
        book_data = valid_book()
        post_resp = client.post("/books", json=book_data, expected_status=201)
        created = post_resp.json()
        model = BookResponseModel.model_validate(created)
        yield model
