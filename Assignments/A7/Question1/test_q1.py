#Assignment 7

## Problem 1 for Question 1

##Test function
import q1

def test_smallest_factor():
    assert q1.smallest_factor(1) == 1
    assert q1.smallest_factor(2) == 2
    assert q1.smallest_factor(3) == 3
    assert q1.smallest_factor(4) == 2
    assert q1.smallest_factor(7) == 7
    assert q1.smallest_factor(11) == 11
    assert q1.smallest_factor(13) == 13
    assert q1.smallest_factor(1000) == 2
    assert q1.smallest_factor(33) == 3
    assert q1.smallest_factor(829) == 829