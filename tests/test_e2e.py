import pytest
import allure
import json
from data.book_payloads import valid_book
from steps.book_steps import create_book, get_book_by_id, update_book, delete_book
from utils.assertions import assert_equals, assert_status_code
from utils.endpoints import BOOKS_ENDP
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
        #create book
        book_id, post_resp = create_book(client, book, tracker=tracker)
        assert_status_code(post_resp, 201, f"POST {BOOKS_ENDP}")
        #get created book
        fetched_book = get_book_by_id(client, book_id)
        assert_equals(fetched_book["title"], book["title"], field="title", context="GET after create")
        assert_equals(fetched_book["pageCount"], book["pageCount"], field="pageCount", context="GET after create")
        #update book
        update_payload = {**book, "description": "Updated Desc"}
        updated_book = update_book(client, book_id, update_payload)
        assert_equals(updated_book["description"], "Updated Desc", field="description", context="PUT")
        assert_equals(updated_book["id"], book_id, field="id", context="PUT")
        #get updated book
        get_updated = get_book_by_id(client, book_id)
        assert_equals(get_updated["description"], "Updated Desc", field="description", context="GET after update")
        #delete and get deleted book
        delete_resp = delete_book(client, book_id, tracker=tracker)
        assert_status_code(delete_resp, 200, f"DELETE {BOOKS_ENDP}/{book_id}")
        get_book_by_id(client, book_id, expected_status=404)
