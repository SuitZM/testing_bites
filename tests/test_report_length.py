from lib.report_length import *

def test_report_length():
    """
    When I give it "football" (8 letters)
    It tells me the string was 8 characters long
    """
    result = report_length("football")
    assert result == "This string was 8 characters long."

def test_report_length_with_spaces():
    """
    When I give it "hi there"
    The space counts too, so it's 8 characters long
    """
    result = report_length("hi there")
    assert result == "This string was 8 characters long."

def test_report_length_empty_string():
    """
    When I give it an empty string ""
    It tells me the string was 0 characters long
    """
    result = report_length("")
    assert result == "This string was 0 characters long."