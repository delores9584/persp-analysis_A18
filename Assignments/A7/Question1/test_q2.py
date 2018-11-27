#Assignment 7

## Problem 2 for Question 1

##Test function
import q2

def test_month_length():
    assert q2.month_length("January", leap_year = False) == 31
    assert q2.month_length("February", leap_year = True) == 29
    assert q2.month_length("February", leap_year = False) == 28
    assert q2.month_length("March", leap_year = False) == 31
    assert q2.month_length("April", leap_year = False) == 30
    assert q2.month_length("May", leap_year = False) == 31
    assert q2.month_length("June", leap_year = False) == 30
    assert q2.month_length("July", leap_year = False) == 31
    assert q2.month_length("August", leap_year = False) == 31
    assert q2.month_length("September", leap_year = False) == 30
    assert q2.month_length("October", leap_year = False) == 31
    assert q2.month_length("November", leap_year = False) == 30
    assert q2.month_length("December", leap_year = False) == 31
    assert q2.month_length("Year") == None