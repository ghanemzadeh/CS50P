import pytest

from fuel import convert, gauge

def test_convert():
    assert convert("3/4") == 75
    assert convert("1/4") == 25

def test_divid_by_zero():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_value_error():
    with pytest.raises(ValueError):
        convert("10/3")

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(80) == "80%"
