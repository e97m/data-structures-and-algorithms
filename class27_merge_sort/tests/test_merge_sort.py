from class27_merge_sort.merge_sort import merge_sort


def test_1():
    assert merge_sort([8,4,23,42,16,15]) == [4, 8, 15, 16, 23, 42]

def test_2():
    assert merge_sort([20,18,12,8,5,-2]) == [-2, 5, 8, 12, 18, 20]

def test_3():
    assert merge_sort([5,12,7,5,5,7]) == [5, 5, 5, 7, 7, 12]

def test_4():
    assert merge_sort([2,3,5,7,13,11]) == [2, 3, 5, 7, 11, 13]

def test_empty():
    assert merge_sort([]) == 'Empty array!'

def test_sting():
    assert merge_sort([2,'1', 5, 3]) == 'Please enter an integer array!'

def test_string_2():
    assert merge_sort([2,'a', 5, 3]) == 'Please enter an integer array!'

def test_boolean():
    assert merge_sort([2,True, 5, 3]) == 'Please enter an integer array!'

def test_boolean_2():
    assert merge_sort([2,False, 5, 3]) == 'Please enter an integer array!'