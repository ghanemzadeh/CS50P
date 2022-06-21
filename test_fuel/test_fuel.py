import pytest

from fuel import convert, gauge

def test_convert():
    assert convert("3/4") == 75
    assert convert("1/4") == 25

    try:
        assert convert("1/0")
        assert convert("10/3")
    except ZeroDivisionError:
        pass
    except ValueError:
        pass

#    try:
#        assert convert("10/3")
#    except ValueError:
#        pass

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(80) == "80%"
