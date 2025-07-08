import pytest
import allure
import json
from data.book_payloads import valid_book
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
        with allure.step("Create a book"):
            post_resp = client.post("/books", json=book, expected_status=201)
            post_data = post_resp.json()
            allure.attach(json.dumps(book, indent=2), name="POST Payload",
                          attachment_type=allure.attachment_type.JSON)
            allure.attach(post_resp.text, name="Response Body", attachment_type=allure.attachment_type.JSON)
            assert "id" in post_data, f"No 'id' field found in {post_data}"
            book_id = post_data["id"]

        with allure.step("Read the created book by id"):
            get_resp = client.get(f"/books/{book_id}", expected_status=200)
            data = get_resp.json()
            allure.attach(get_resp.text, name="Fetched Book", attachment_type=allure.attachment_type.JSON)
            assert data.get("title") == book["title"], f"Title mismatch"
            assert data.get("pageCount") == book["pageCount"], f"Page count mismatch"

        with allure.step("Update the book via PUT"):
            updated_data = {**book, "description": "Updated Desc"}
            put_resp = client.put(f"/books/{book_id}", json=updated_data, expected_status=200)
            put_data = put_resp.json()
            allure.attach(json.dumps(updated_data, indent=2), name="PUT payload",
                          attachment_type=allure.attachment_type.JSON)
            allure.attach(put_resp.text, name="Updated Response", attachment_type=allure.attachment_type.JSON)
            assert put_data.get("description") == "Updated Desc"
            assert put_data.get("id") == book_id

        with allure.step("Confirm update via GET by id"):
            get_updated = client.get(f"/books/{book_id}", expected_status=200)
            get_data = get_updated.json()
            allure.attach(json.dumps(get_data, indent=2), name="Updated Book",
                          attachment_type=allure.attachment_type.JSON)
            assert get_data.get("description") == "Updated Desc"

        with allure.step("Delete the book and validate it is gone"):
            del_resp = client.delete(f"/books/{book_id}", expected_status=200)
            allure.attach(del_resp.text, "Delete Response", allure.attachment_type.JSON)
            client.get(f"/books/{book_id}", expected_status=404)
