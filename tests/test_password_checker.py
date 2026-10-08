import pytest
from lib.password_checker import *

def test_password_equal_to_or_longer_than_8():
    """
    When I check a password that's exactly 8 characters
    It's valid, so check returns True
    """
    pw = PasswordChecker()
    result = pw.check("password")
    assert result == True

def test_password_less_than_8_to_raise_error():
    """
    When I check a password that's only 7 characters
    It raises an error: "Invalid password, must be 8+ characters."
    """
    pw = PasswordChecker()
    with pytest.raises(Exception) as e:
        pw.check("passwor")
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters."