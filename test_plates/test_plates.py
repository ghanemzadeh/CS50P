import pytest

from plates import is_valid

def test_letters():
    assert value("CS50") == True


def test_length():
    assert value("TP") == True
    assert value("H") == False
    assert value("OUTATIME") == False
    assert value("Abadan") == True

def test_numbers():
    assert value("CS50P") == False
    assert value("CS05") == False

def test_punctuation():
    assert value("PI3.14") == False
