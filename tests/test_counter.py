from lib.counter import *

def test_counter():
    counter = Counter()
    result = counter.report()
    assert result == "Counted to 0 so far."

def test_counter_add():
    counter = Counter()
    counter.add(10)
    result = counter.report()
    assert result == "Counted to 10 so far."

def test_counter_add_twice():
    counter = Counter()
    counter.add(10)
    counter.add(5)
    result = counter.report()
    assert result == "Counted to 15 so far."