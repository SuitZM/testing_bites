from lib.string_builder import *

def test_string_builder():
    """
    When I make a new string builder and add nothing
    The output is an empty string
    """
    builder = StringBuilder()
    result = builder.output()
    assert result == ""

def test_add_string_builder():
    """
    When I add "hello" and then " world"
    The output joins them: "hello world"
    """
    builder = StringBuilder()
    builder.add("hello")
    builder.add(" world")
    result = builder.output()
    assert result == "hello world"

def test_size_string_builder():
    """
    When I add "hello" and then " world"
    The size is 11, because the space counts as a character
    """
    builder = StringBuilder()
    builder.add("hello")
    builder.add(" world")
    result = builder.size()
    assert result == 11

