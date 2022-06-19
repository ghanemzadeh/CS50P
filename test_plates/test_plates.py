import pytest

from plates import is_valid

def test_letters():
    assert is_valid("CS50") == True
    assert is_valid("AAA") == True
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False

def test_length():
    assert is_valid("TP") == True
    assert is_valid("H") == False
    assert is_valid("OUTATIME") == False
    assert is_valid("Abadan") == True

def test_numbers():
    assert is_valid("CS50P") == False
    assert is_valid("CS05") == False
    assert is_valid("52A") == False

def test_punctuation():
    assert is_valid("PI3.14") == False
