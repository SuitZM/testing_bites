from lib.greet import *

def test_greet_name():
    """
    When I greet "Connie Camps"
    I get back "Hello, Connie Camps!"
    """
    result = greet("Connie Camps")
    assert result == "Hello, Connie Camps!"