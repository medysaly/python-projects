from bank import value
import pytest

def test_hello():
    assert value("hello") == 0

def test_hi():
    assert value("hi") == 20

def test_else():
    assert value("ciao") == 100

def test_capital():
    assert value("HELLO") == 0