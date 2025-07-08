import requests
import os
from config.env_config import BASE_URL

def main():
    session = requests.Session()
    url = f"{BASE_URL}/books"
    resp = session.get(url)
    resp.raise_for_status()
    books = resp.json()
    deleted = 0

    for book in books:
        title = book.get("title", "")
        if title.startswith("[TEST]"):
            book_id = book["id"]
            del_resp = session.delete(f"{url}/{book_id}")
            if del_resp.status_code in (200, 204, 404):
                print(f"Deleted test book id={book_id}")
                deleted += 1
            else:
                print(f"WARNING: Could not delete book {book_id}: {del_resp.status_code} {del_resp.text}")

    print(f"Total deleted: {deleted}")

if __name__ == "__main__":
    main()
