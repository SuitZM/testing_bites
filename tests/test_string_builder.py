from lib.string_builder import *

def test_string_builder():
    builder = StringBuilder()
    result = builder.output()
    assert result == ""

def test_add_string_builder():
    builder = StringBuilder()
    builder.add("hello")
    builder.add(" world")
    result = builder.output()
    assert result == "hello world"

def test_size_string_builder():
    builder = StringBuilder()
    builder.add("hello")
    builder.add(" world")
    result = builder.size()
    assert result == 11

