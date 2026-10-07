from lib.gratitudes import *

def test_gratitudes():
    gratitudes = Gratitudes()
    result = gratitudes.format()
    assert result == "Be grateful for: "

def test_add_to_gratitudes():
    gratitudes = Gratitudes()
    gratitudes.add("the end of the day")
    result = gratitudes.format()
    assert result == "Be grateful for: the end of the day"

def test_add_twice_to_gratitudes():
        gratitudes = Gratitudes()
        gratitudes.add("fish")
        gratitudes.add("chips")
        result = gratitudes.format()
        assert result == "Be grateful for: fish, chips"