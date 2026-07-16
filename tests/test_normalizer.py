from searchforge.normalizer import Normalizer


def test_basic_normalization():
    normalizer = Normalizer()

    result = normalizer.normalize(
        "  Hello, Django!!!  "
    )

    assert result == "hello django"


def test_unicode_cleanup():
    normalizer = Normalizer()

    result = normalizer.normalize(
        "Café"
    )

    assert result == "cafe"


def test_lowercase_disable():
    normalizer = Normalizer(lowercase=False)

    result = normalizer.normalize(
        "Django"
    )

    assert result == "Django"


def test_invalid_input():
    normalizer = Normalizer()

    try:
        normalizer.normalize(123)
    except TypeError:
        assert True
    else:
        assert False
