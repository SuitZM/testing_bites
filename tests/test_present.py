import pytest
from lib.present import *

def test_wrapping_twice_raises_error():
    """
    When I wrap a sock and then try to wrap another
    It raises an error: "A contents has already been wrapped."
    """
    present = Present()
    present.wrap("sock")
    with pytest.raises(Exception) as e: 
        present.wrap("sock")
    error_message = str(e.value)
    assert error_message == "A contents has already been wrapped."

def test_unwrapping_empty_present_raises_error():
    """
    When I try to unwrap a present that was never wrapped
    It raises an error: "No contents have been wrapped."
    """
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    error_message = str(e.value)
    assert error_message == "No contents have been wrapped."

# Note: at first I wrote unwrap("sock"), which raised a TypeError instead.
# pytest.raises still caught it, but the message check failed. That's why
# we always check the error message, not just that an error happened.

def test_wrap_then_unwrap():
    """
    When I wrap a sock and then unwrap it
    I get the sock back
    """
    present = Present()
    present.wrap("sock")
    result = present.unwrap()
    assert result == "sock"