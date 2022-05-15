import pytest
from class15_trees.ktree import  KNode, KAryTree


def test_empty_KAryTree():
    tree = KAryTree()
    assert tree.root == None

def test_insert_k(my_KT):
    assert my_KT.breadth_first_k() == [5, 2, 10, 1, 1, 3, 4, 7, 12, 15]

def test_fizz_buzz_tree(my_KT):
    assert my_KT.fizz_buzz_tree().breadth_first_k() == ['Buzz', '2', 'Buzz', '1', '1', 'Fizz', '4', '7', 'Fizz', 'FizzBuzz']

def test_empty_fizzbuzz():
    tree = KAryTree()
    with pytest.raises(Exception):
        assert tree.fizz_buzz_tree()

def test_fizzbuzz_error():
    tree = KNode(5)
    with pytest.raises(Exception):
        assert tree.fizz_buzz_tree()


@pytest.fixture
def my_KT():
    the_tree = KAryTree()
    the_tree.insert_k(5, 1)
    [the_tree.insert_k(x,3) for x in [2,10,1,1,3, 4, 7,12, 15]]
    return the_tree
    
    # tree.insert_k(2, 3)
    # tree.insert_k(10, 3)
    # tree.insert_k(1, 3)
    # tree.insert_k(1, 3)
    # tree.insert_k(3, 3)
    # tree.insert_k(4, 3)
    # tree.insert_k(7, 3)
    # tree.insert_k(12, 3)
    # tree.insert_k(15, 3)