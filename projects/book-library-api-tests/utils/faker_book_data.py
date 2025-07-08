import uuid
from faker import Faker
from datetime import datetime
from typing import Any, Dict, List, Optional

fake = Faker()


class BookGenerator:
    """
    Generates fake book payloads for testing.
    Allows overriding default field values.
    """

    def generate_book(self, overrides: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Generate a single fake book object
        overrides: Optional dict to override generated fields
        """
        data = {
            "id": abs(hash(uuid.uuid4())) % 10_000_000,
            "title": f"[TEST] {fake.sentence(nb_words=4)}",
            "description": fake.text(max_nb_chars=100),
            "pageCount": fake.random_int(min=1, max=500),
            "excerpt": fake.text(max_nb_chars=50),
            "publishDate": datetime.now().isoformat()
        }

        if overrides:
            data.update(overrides)

        return data

    def generate_books(self, count: int, overrides: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """
        Generate multiple fake book objects
        count: Number of books to generate.
        overrides: Optional dict to override fields for all books.
        """
        return [self.generate_book(overrides) for _ in range(count)]
