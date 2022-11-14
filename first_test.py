# https://www.youtube.com/watch?v=byaxg00Gf9I
import pytest

def func(x):
    return x + 5

# pytest first_test.py
def test_method():
    assert func(3) == 8
