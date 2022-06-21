import pytest

from fuel import convert, gauge

def test_convert():
    assert convert("3/4") == 75
    assert convert("1/4") == 25
    try:
        convert("1/0")
    except ZeroDivisionError as exc:
        assert False, f"Divide by zero Error {exc}"

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(80) == "80%"
