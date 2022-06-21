import pytest

from fuel import convert, gauge

def test_convert():
    assert convert("3/4") == 75
    assert convert("1/4") == 25
    with pytest.raises(MissingBothCoordException):
>           sum_x_y(data)

def test_gauge():