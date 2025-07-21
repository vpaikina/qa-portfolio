from utils.resource_tracker import ResourceTracker
from utils.endpoints import BOOKS


def assert_status_code(response, expected_status, error_prefix="", payload=None):
    if response.status_code != expected_status:
        msg = f"{error_prefix}: expected {expected_status}, got {response.status_code}\n"
        if payload is not None:
            msg += f"Payload: {payload}\n"
        msg += f"Response: {response.text}"
        raise AssertionError(msg)


def safe_json(response, error_prefix=""):
    try:
        return response.json()
    except Exception as e:
        raise AssertionError(
            f"{error_prefix}: invalid JSON in response.\n"
            f"Status: {response.status_code}\n"
            f"Response: {getattr(response, 'text', '')}"
        ) from e


def create_book(client, payload, tracker: ResourceTracker = None, expected_status=201):
    response = client.post(BOOKS, json=payload, expected_status=expected_status)
    assert_status_code(response, expected_status, error_prefix="POST {BOOKS}", payload=payload)
    data = safe_json(response, error_prefix="POST {BOOKS}")
    try:
        book_id = data["id"]
    except (KeyError, ValueError, TypeError) as e:
        raise AssertionError(
            f"POST /books: missing or invalid 'id' in response.\n"
            f"Response: {data}"
        ) from e
    if tracker:
        tracker.track_create(book_id)
    return book_id, data


def get_book_by_id(client, book_id, expected_status=200):
    response = client.get(f"{BOOKS}/{book_id}", expected_status=expected_status)
    assert_status_code(response, expected_status, error_prefix=f"GET {BOOKS}/{book_id}")
    return safe_json(response, error_prefix=f"GET {BOOKS}/{book_id}")


def update_book(client, book_id, updated_data, expected_status=200):
    response = client.put(f"{BOOKS}/{book_id}", json=updated_data, expected_status=expected_status)
    assert_status_code(response, expected_status, error_prefix=f"PUT {BOOKS}/{book_id}", payload=updated_data)
    return safe_json(response, error_prefix=f"PUT {BOOKS}/{book_id}")


def delete_book(client, book_id, tracker: ResourceTracker = None, expected_status=200):
    response = client.delete(f"{BOOKS}/{book_id}", expected_status=expected_status)
    if response.status_code not in [expected_status, 404]:
        assert_status_code(response, expected_status, error_prefix=f"DELETE {BOOKS}/{book_id}")
    if tracker:
        tracker.track_delete(book_id)
    return response
