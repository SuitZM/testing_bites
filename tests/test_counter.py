from lib.counter import *

def test_counter():
    """
    When I make a new counter and add nothing
    The report says it has counted to 0
    """
    counter = Counter()
    result = counter.report()
    assert result == "Counted to 0 so far."

def test_counter_add():
    """
    When I make a new counter and add 10
    The report says it has counted to 10
    """
    counter = Counter()
    counter.add(10)
    result = counter.report()
    assert result == "Counted to 10 so far."

def test_counter_add_twice():
    """
    When I add 10 and then 5
    The counter remembers both, so it says 15
    """
    counter = Counter()
    counter.add(10)
    counter.add(5)
    result = counter.report()
    assert result == "Counted to 15 so far."