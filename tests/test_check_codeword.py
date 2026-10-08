from lib.check_codeword import *

def test_check_codeword():
    """
    When the codeword is exactly "horse"
    I'm let in: "Correct! Come in."
    """
    result = check_codeword("horse")
    assert result == "Correct! Come in."

def test_close_codeword():
    """
    When the codeword starts with "h" and ends with "e" but isn't "horse"
    I'm told I'm close: "Close, but nope."
    """
    result = check_codeword("house")
    assert result == "Close, but nope."

def test_wrong_codeword():
    """
    When the codeword is anything else, like "cat"
    I'm told it's wrong: "WRONG!"
    """
    result = check_codeword("cat")
    assert result == "WRONG!"