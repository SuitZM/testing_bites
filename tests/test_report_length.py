from lib.report_length import *

def test_report_length():
    result = report_length("football")
    assert result == "This string was 8 characters long."

def test_report_length_with_spaces():
    result = report_length("hi there")
    assert result == "This string was 8 characters long."

def test_report_length_empty_string():
    result = report_length("")
    assert result == "This string was 0 characters long."