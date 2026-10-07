from lib.counter import *

def test_counter():
    counter = Counter()
    result = counter.report()
    assert result == "Counted to 0 so far."
