import pytest
from class33_hashmap_leftjoin.left_join import left_join


def test_left_join(left, right):
    assert left_join(left, right) == {'a': '1,4', 'b': '2,5', 'c': '3,NULL'}

def test_left_join_emptyLeft( right):
    left = {}
    assert left_join(left, right) == {}

def test_left_join_emptyRight(left):
    right = {}
    assert left_join(left, right) == {'a': '1,NULL', 'b': '2,NULL', 'c': '3,NULL'}

def test_join_empty():
    left = {}
    right = {}
    assert left_join(left, right) == {}



@pytest.fixture
def left():
    left_table = {'a': '1', 'b': '2', 'c': '3'}
    return left_table

@pytest.fixture
def right():
    right_table = {'a': '4', 'b': '5', 'd': '6'}
    return right_table