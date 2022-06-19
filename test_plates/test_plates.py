import pytest

from plates import is_valid

def test_letters():
    assert value("CS50") == True
    assert value("Hello, Newman") == 0
    assert value("How you doing?") == 20
    assert value("What's happening?") == 100

def test_length():
    assert value("Hello") == 0

def test_numbers():
    assert value("Hello") == 0

def test_punctuation():
    assert value("Hello") == 0
