from lib.check_codeword import *

def test_check_codeword():
    result = check_codeword("horse")
    assert result == "Correct! Come in."

def test_close_codeword():
    result = check_codeword("house")
    assert result == "Close, but nope."

def test_wrong_codeword():
    result = check_codeword("cat")
    assert result == "WRONG!"