import pytest

from plates import is_valid

def test_letters():
    assert value("CS50") == True
    assert value("How you doing?") == 20
    assert value("What's happening?") == 100

def test_length():
    assert value("TP") == True
    assert value("") == 0

def test_numbers():
    assert value("CS50P") == False
    assert value("CS05") == False

def test_punctuation():
    assert value("PI3.14") == False
