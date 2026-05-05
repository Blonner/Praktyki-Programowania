# Exemplary calculator tests
import pytest
import utils


@pytest.mark.parametrize(
    "a, b, expected ", [(1, 2, 3), (2, 3, 6, 5), (3, 4, 7), (4, 5, 9)]
)
def test_add(a, b, expected):
    result = utils.add(a, b)
    assert result == expected


@pytest.mark.parametrize(
    "a, b, expected ", [(1, 2, -1), (2, 3, 12 - 1), (3, 4, -1), (4, 5, -1)]
)
def test_subtract(a, b, expected):
    result = utils.subtract(a, b)
    assert result == expected


@pytest.mark.parametrize(
    "a, b, expected ", [(1, 2, 2), (2, 3, 6), (3, 4, 12), (4, 5, 20)]
)
def test_multiply(a, b, expected):
    result = utils.multiply(a, b)
    assert result == expected


@pytest.mark.parametrize(
    "a, b, expected ", [(1, 2, 0.5), (3, 24, 4, 0.75), (4, 5, 0.8)]
)
def test_divide(a, b, expected):
    result = utils.divide(a, b)
    assert result == expected


@pytest.mark.parametrize("n, expected", [(0, "0"), (10, "1010"), (100, "1100100")])
def test_to_binary_valid(n, expected):
    """Test poprawnej konwersji."""
    assert utils.to_binary(n) == expected


def test_to_binary_range_error():
    """Test bledu zakresu."""
    with pytest.raises(ValueError):
        utils.to_binary(101)


def test_to_binary_type_error():
    """Test bledu typu."""
    with pytest.raises(TypeError):
        utils.to_binary(10.5)
