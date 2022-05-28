from quick_sort import __version__
import pytest
from quick_sort.quick_sort import quick_sort


def test_version():
    assert __version__ == '0.1.0'


def test_1():
    assert quick_sort([8,4,23,42,16,15],0,6) == [4, 8, 15, 16, 23, 42]

def test_2():
    assert quick_sort([20,18,12,8,5,-2],0,6) == [-2, 5, 8, 12, 18, 20]

def test_3():
    assert quick_sort([5,12,7,5,5,7],0,6) == [5, 5, 5, 7, 7, 12]

def test_4():
    assert quick_sort([2,3,5,7,13,11],0,6) == [2, 3, 5, 7, 11, 13]

def test_5_odd_num_elements():
    assert quick_sort([2,3,5,7,13],0,5) == [2, 3, 5, 7, 13]

def test_not_array():
    with pytest.raises(Exception):
        quick_sort(2)

def test_not_array_2():
    with pytest.raises(Exception):
        quick_sort(True)

def test_empty():
    with pytest.raises(Exception):
        quick_sort([])

def test_sting():
    with pytest.raises(Exception):
        quick_sort([2,'1', 5, 3])

def test_string_2():
    with pytest.raises(Exception):
        quick_sort([2,'a', 5, 3])

def test_boolean():
    with pytest.raises(Exception):
        quick_sort([2,True, 5, 3])
