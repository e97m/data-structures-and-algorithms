import pytest
from class33_hashmap_leftjoin.left_join import left_join, left_join_arr


def test_left_join(left_dict, right_dict):
    assert left_join(left_dict, right_dict) == {'a': '1,4', 'b': '2,5', 'c': '3,NULL'}

def test_left_join_emptyLeft(right_dict):
    left_dict = {}
    assert left_join(left_dict, right_dict) == {}

def test_left_join_emptyRight(left_dict):
    right_dict = {}
    assert left_join(left_dict, right_dict) == {'a': '1,NULL', 'b': '2,NULL', 'c': '3,NULL'}

def test_join_empty():
    left_dict = {}
    right_dict = {}
    assert left_join(left_dict, right_dict) == {}


def test_left_join_arr(left_arr, right_arr):
    assert left_join_arr(left_arr, right_arr) == [['a', '1', '4'], ['b', '2', '5'], ['c', '3', None]]

def test_left_join_arr_emptyLeft(right_arr):
    left_arr = []
    assert left_join_arr(left_arr, right_arr) == []

def test_left_join_arr_emptyRight(left_arr):
    right_arr = []
    assert left_join_arr(left_arr, right_arr) == [['a', '1', None], ['b', '2', None], ['c', '3', None]]

def test_left_join_arr_empty():
    left_arr = []
    right_arr = []
    assert left_join_arr(left_arr, right_arr) == []


@pytest.fixture
def left_dict():
    left_table = {'a': '1', 'b': '2', 'c': '3'}
    return left_table

@pytest.fixture
def right_dict():
    right_table = {'a': '4', 'b': '5', 'd': '6'}
    return right_table

@pytest.fixture
def left_arr():
    left = [['a','1'],['b','2'],['c','3']]
    return left

@pytest.fixture
def right_arr():
    right = [['a','4'],['b','5'],['d','6']]
    return right