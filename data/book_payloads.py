from utils.faker_book_data import BookGenerator

_generator = BookGenerator()


def valid_book(**overrides):
    return _generator.generate_book(overrides)


def book_missing_description():
    return valid_book(description=None)


def book_empty_description_field():
    return valid_book(description="")


def book_missing_pageCount():
    return valid_book(pageCount=None)


def book_empty_pageCount_field():
    return valid_book(pageCount="")


def book_missing_publishDate():
    return valid_book(pageCount=None)


def book_empty_publishDate_field():
    return valid_book(pageCount="")


def book_negative_page_count():
    return valid_book(pageCount=-100)


def book_with_long_title():
    return valid_book(title="[TEST]" * 100)


def book_with_long_description():
    return valid_book(description="A" * 1000)


def book_with_non_integer_pageCount():
    return valid_book(pageCount="not-a-number")
