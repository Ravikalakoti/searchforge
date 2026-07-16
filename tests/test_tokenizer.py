from searchforge.tokenizer import Tokenizer


def test_basic_tokenization():
    tokenizer = Tokenizer()

    result = tokenizer.tokenize(
        "Hello, Django Developer!"
    )

    assert result == [
        "hello",
        "django",
        "developer",
    ]


def test_lowercase_disable():
    tokenizer = Tokenizer(lowercase=False)

    result = tokenizer.tokenize(
        "Hello Django"
    )

    assert result == [
        "Hello",
        "Django",
    ]


def test_unicode_normalization():
    tokenizer = Tokenizer()

    result = tokenizer.tokenize(
        "Ｄjango"
    )

    assert result == [
        "django",
    ]


def test_invalid_input():
    tokenizer = Tokenizer()

    try:
        tokenizer.tokenize(123)
    except TypeError:
        assert True
    else:
        assert False
