import add_sum
import pytest
def test_add():
    assert add_sum.add(4,5)==9  # assert only returns boolean values like True or False
    assert add_sum.add(9,7)==16
def test_sub():
    assert add_sum.sub(6,1)==5