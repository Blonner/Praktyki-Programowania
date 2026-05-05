"""
Exemplary calculator functions
"""


def add(a: int, b: int) -> int:
    """Suma:"""
    return a + b


def subtract(a: int, b: int) -> int:
    """Różnica:"""
    return a - b


def multiply(a: int, b: int) -> int:
    """Iloczyn:"""
    return a * b


def divide(a: int, b: int) -> float:
    """Iloraz:"""
    return a / b


def to_binary(n: int) -> str:
    """Konwersja na system binarny."""
    if not isinstance(n, int):
        raise TypeError("To nie jest liczba calkowita.")
    if not 0 <= n <= 100:
        raise ValueError("Liczba poza zakresem 0-100.")
    return bin(n)[2:]
