import pytest
import allure
import json
from data.book_payloads import valid_book
from steps.book_steps import create_book, get_book_by_id, update_book, delete_book
from utils.resource_tracker import tracked_client

# ---- check E2E scenario ----

@allure.epic("Book Management")
@allure.feature("End-to-End CRUD Operations")
@allure.story("US-1 User can create, read, update, and delete a book")
@allure.description("""
End-to-end scenario that covers the full lifecycle of a book: 
creation, retrieval, update, and deletion.
""")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
@pytest.mark.e2e
def test_book_crud_e2e(api_client):
    book = valid_book()
    with tracked_client(api_client) as (client, tracker):
        with allure.step("Create book"):
            book_id, post_data = create_book(client, book, tracker=tracker)
            allure.attach(json.dumps(book, indent=2), name="POST Payload",
                          attachment_type=allure.attachment_type.JSON)
            allure.attach(json.dumps(post_data, indent=2), name="Response Body",
                          attachment_type=allure.attachment_type.JSON)

        with allure.step("Get created book by id"):
            fetched_book = get_book_by_id(client, book_id)
            allure.attach(json.dumps(fetched_book, indent=2), name="Fetched Book",
                          attachment_type=allure.attachment_type.JSON)
            assert fetched_book.get("title") == book["title"], "Title mismatch"
            assert fetched_book.get("pageCount") == book["pageCount"], "Page count mismatch"

        with allure.step("Update book"):
            update_payload = {**book, "description": "Updated Desc"}
            put_response = update_book(client, book_id, update_payload)
            allure.attach(json.dumps(update_payload, indent=2), name="PUT payload",
                          attachment_type=allure.attachment_type.JSON)
            allure.attach(json.dumps(put_response, indent=2), name="Updated Response",
                          attachment_type=allure.attachment_type.JSON)
            assert put_response.get("description") == "Updated Desc"
            assert put_response.get("id") == book_id

        with allure.step("Get updated book"):
            get_updated = get_book_by_id(client, book_id)
            allure.attach(json.dumps(get_updated, indent=2), name="Updated Book",
                          attachment_type=allure.attachment_type.JSON)
            assert get_updated.get("description") == "Updated Desc"

        with allure.step("Delete the book and validate it is gone"):
            delete_resp = delete_book(client, book_id, tracker=tracker)
            allure.attach(delete_resp.text, "Delete Response", allure.attachment_type.JSON)
            get_book_by_id(client, book_id, expected_status=404)
