from curses.ascii import isdigit         # Applied TDD (Test driven development) where we write test case first then write the code
import pytest
import findstring
def test_present():
    assert findstring.ispresent("Animesh")
def test_isdigit():
    assert findstring.nodigit('A1') # here test will fail because argument has alphabatic and numaric which return False