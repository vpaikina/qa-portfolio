import allure

from schemas.book import BookResponseModel
from utils.assertions import assert_status_code, assert_has_field, assert_valid_json, assert_response_by_schema
from utils.resource_tracker import ResourceTracker
from utils.endpoints import BOOKS_ENDP
import json


def get_response_json(response, context: str = ""):
    with allure.step(f"Parse response JSON [{context}]"):
        data = assert_valid_json(response, context=context)
        allure.attach(json.dumps(data, indent=2), "Parsed JSON", allure.attachment_type.JSON)
        return data


def create_book(client, payload, tracker: ResourceTracker = None, expected_status=201):
    with allure.step("Create book"):
        response = client.post(BOOKS_ENDP, json=payload, expected_status=expected_status)
        allure.attach(json.dumps(payload, indent=2), "POST Payload", allure.attachment_type.JSON)
        allure.attach(response.text, "POST Response", allure.attachment_type.JSON)
        assert_status_code(response, expected_status, context=f"POST {BOOKS_ENDP}", payload=payload)
        data = get_response_json(response, context=f"POST {BOOKS_ENDP}")
        assert_has_field(data, "id", context=f"POST {BOOKS_ENDP}")
        book_id = data["id"]
        if tracker:
            tracker.track_create(book_id)
        return book_id, response


def get_book_by_id(client, book_id, expected_status=200):
    with allure.step(f"Get book by id={book_id}"):
        response = client.get(f"{BOOKS_ENDP}/{book_id}", expected_status=expected_status)
        allure.attach(response.text, "GET Response", allure.attachment_type.JSON)
        assert_status_code(response, expected_status, context=f"GET {BOOKS_ENDP}/{book_id}")
        return get_response_json(response, context=f"GET {BOOKS_ENDP}/{book_id}")


def update_book(client, book_id, updated_data, expected_status=200):
    with allure.step(f"Update book id={book_id}"):
        response = client.put(f"{BOOKS_ENDP}/{book_id}", json=updated_data, expected_status=expected_status)
        allure.attach(json.dumps(updated_data, indent=2), "PUT Payload", allure.attachment_type.JSON)
        allure.attach(response.text, "PUT Response", allure.attachment_type.JSON)
        assert_status_code(response, expected_status, context=f"PUT {BOOKS_ENDP}/{book_id}", payload=updated_data)
        return get_response_json(response, context=f"PUT {BOOKS_ENDP}/{book_id}")


def delete_book(client, book_id, tracker: ResourceTracker = None, expected_status=200):
    with allure.step(f"Delete book by id={book_id}"):
        response = client.delete(f"{BOOKS_ENDP}/{book_id}", expected_status=expected_status)
        allure.attach(response.text, "DELETE Response", allure.attachment_type.JSON)
        if response.status_code not in [expected_status, 404]:
            assert_status_code(response, expected_status, context=f"DELETE {BOOKS_ENDP}/{book_id}")
        if tracker:
            tracker.track_delete(book_id)
        return response


def assert_book_contract(response_json, context: str = ""):
    assert_response_by_schema(response_json, BookResponseModel, context)
