import pytest

from fuel import convert, gauge

def test_convert():
    assert convert("3/4") == 75
    assert convert("1/4") == 25

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(90) == "F"
    assert gauge(100) == "F"
    assert gauge(80) == "80%"
