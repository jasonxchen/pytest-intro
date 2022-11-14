import pytest

# pytest multiple_tests.py -k method1
@pytest.mark.one    # pytest multiple_tests.py -m one
def test_method1():
    x = 5
    y = 10
    assert x == y

# pytest multiple_tests.py -k method2
@pytest.mark.two    # pytest multiple_tests.py -m two
def test_method2():
    a = 15
    b = 20
    assert a + 5 == b
