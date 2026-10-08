from lib.gratitudes import *

def test_gratitudes():
    """
    When I haven't added any gratitudes
    It just shows "Be grateful for: " (with a space at the end)
    """
    gratitudes = Gratitudes()
    result = gratitudes.format()
    assert result == "Be grateful for: "

def test_add_to_gratitudes():
    """
    When I add one gratitude
    It appears straight after "Be grateful for: "
    """
    gratitudes = Gratitudes()
    gratitudes.add("the end of the day")
    result = gratitudes.format()
    assert result == "Be grateful for: the end of the day"

# Note: this test was accidentally indented inside the one above at first,
# so pytest couldn't see it (still 15 collected). Check the count goes up!
def test_add_twice_to_gratitudes():
    """
    When I add "fish" and then "chips"
    They're shown with a comma and space between: "fish, chips"
    """
    gratitudes = Gratitudes()
    gratitudes.add("fish")
    gratitudes.add("chips")
    result = gratitudes.format()
    assert result == "Be grateful for: fish, chips"