from class26_insertion_sort.insertion_sort import insertion_sort


def test_1():
    assert insertion_sort([8,4,23,42,16,15]) == [4, 8, 15, 16, 23, 42]

def test_2():
    assert insertion_sort([20,18,12,8,5,-2]) == [-2, 5, 8, 12, 18, 20]

def test_3():
    assert insertion_sort([5,12,7,5,5,7]) == [5, 5, 5, 7, 7, 12]

def test_4():
    assert insertion_sort([2,3,5,7,13,11]) == [2, 3, 5, 7, 11, 13]

def test_empty():
    assert insertion_sort([]) == 'Empty array!'

def test_sting():
    assert insertion_sort([2,'1', 5, 3]) == 'Please enter an integer array!'

def test_string_2():
    assert insertion_sort([2,'a', 5, 3]) == 'Please enter an integer array!'

def test_boolean():
    assert insertion_sort([2,True, 5, 3]) == 'Please enter an integer array!'

def test_boolean_2():
    assert insertion_sort([2,False, 5, 3]) == 'Please enter an integer array!'