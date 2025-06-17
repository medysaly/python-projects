from twttr import shorten
import pytest

def test_lowercase():
    assert shorten("twitter") == "twttr"

def test_uppercase():
    assert shorten("TWITTER") == "TWTTR"

def test_number():
    assert shorten("1 2 3") == "1 2 3"

def test_punctuation():
    assert shorten(", .") == " , ."

