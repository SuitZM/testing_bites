from lib.greet import *

def test_greet_name():
    result = greet("Connie Camps")
    assert result == "Hello, Connie Camps!"