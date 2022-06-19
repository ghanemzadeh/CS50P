import pytest

from twttr import shorten


def test_shorten():
    assert shorten("Twitter") == "Twttr"
    assert shorten("What's your name?") == "Wht's yr nm?"
    assert shorten("This is 1 tesT dor 2nd time") == "Ths s 1 tsT dr 2nd tm"
    assert shorten("This Is A Test") == "Ths s  Tst"

