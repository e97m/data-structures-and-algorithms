import pytest
from class15_trees.ktree import  KNode, KAryTree, fizz_buzz_tree


def test_empty_KAryTree():
    tree = KAryTree()
    assert tree.root == None

def test_KArayTree(my_KT):
    assert my_KT.breadth_first_k() == [5, 3, 2, 4, 1, 0, 6, 15]

def test_fizz_buzz_tree(my_KT):
    assert fizz_buzz_tree(my_KT) == ['Buzz', '2', 'Buzz', '1', '1', 'Fizz', '4', '7', 'Fizz', 'FizzBuzz']




@pytest.fixture
def my_KT():
    tree = KAryTree()
    tree.root = KNode(5)
    tree.root.children = KNode(3), KNode(2), KNode(4)
    tree.root.children[0].children = KNode(1), KNode(0)
    tree.root.children[2].children = KNode(6), KNode(15)