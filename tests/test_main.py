from didactic_invention.main import generate_message


def test_generate_message_default() -> None:
    assert generate_message() == "Hello, world! Welcome to didactic invention."


def test_generate_message_with_name() -> None:
    assert generate_message("Alice") == "Hello, Alice! Welcome to didactic invention."
