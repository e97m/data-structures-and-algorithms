import pytest
from class15_trees.tree import BinaryTree, BinarySearchTree, TNode

def test_empty():
    tree = BinaryTree()
    assert tree.root == None

def test_empty_binary_search():
    tree = BinarySearchTree()
    assert tree.root == None

def test_manual_insert():
    tree = BinaryTree()
    tree.root = TNode(5)
    tree.root.left = TNode(2)
    tree.root.right = TNode(10)
    tree.root.left.left = TNode(1)
    tree.root.left.right = TNode(3)
    tree.root.right.left = TNode(7)
    tree.root.right.right = TNode(12)
    assert tree.pre_order() == [5, 2, 1, 3, 10, 7, 12]


def test_insert():
    tree = BinarySearchTree()
    tree.insert(5)
    assert tree.pre_order() == [5]

def test_insert_2():
    tree = BinarySearchTree()
    [tree.insert(x) for x in [5,2,1,3,10]]
    assert tree.pre_order() == [5, 2, 1, 3, 10]

def test_insert_TNode():
    tree = BinarySearchTree()
    assert tree.insert(TNode(5)) == 'Please enter a value, it will be converted automaticly to TNode'

def test_find_True(my_tree):
    assert my_tree.find(5) == True

def test_find_False(my_tree):
    assert my_tree.find(6) == False

def test_find_empty():
    tree = BinarySearchTree()
    assert tree.find(5) == 'The tree is empty'

def test_pre_order(my_tree):
    assert my_tree.pre_order() == [5, 2, 1, 3, 10, 7, 12]

def test_pre_order_empty():
    tree = BinarySearchTree()
    assert tree.pre_order() == 'The tree is empty'

def test_pre_order_recursive(my_tree):
    assert my_tree.pre_order_recursive() == [5, 2, 1, 3, 10, 7, 12] 

def test_pre_order_recursive_empty():
    tree = BinarySearchTree()
    assert tree.pre_order_recursive() == 'The tree is empty'

def test_in_order(my_tree):
    assert my_tree.in_order() == [1, 2, 3, 5, 7, 10, 12]

def test_in_order_empty():
    tree = BinarySearchTree()
    assert tree.in_order() == 'The tree is empty'

def test_in_order_recursive(my_tree):
    assert my_tree.in_order_recursive() == [1, 2, 3, 5, 7, 10, 12]

def test_in_order_recursive_empty():
    tree = BinarySearchTree()
    assert tree.in_order_recursive() == 'The tree is empty'

def test_post_order(my_tree):
    assert my_tree.post_order() == [1, 3, 2, 7, 12, 10, 5]

def test_post_order_empty():
    tree = BinarySearchTree()
    assert tree.post_order() == 'The tree is empty'

def test_post_order_recursive(my_tree):
    assert my_tree.post_order_recursive() == [1, 3, 2, 7, 12, 10, 5]

def test_post_order_recursive_empty():
    tree = BinarySearchTree()
    assert tree.post_order_recursive() == 'The tree is empty'

def test_maximum_value():
    tree = BinaryTree()
    tree.root = TNode(10)
    tree.root.left = TNode(12)
    tree.root.right = TNode(5)
    tree.root.left.left = TNode(2)
    tree.root.left.right = TNode(15)
    assert tree.maximum_value() == 15

def test_maximum_value_empty():
    tree = BinaryTree()
    assert tree.maximum_value() == 'The tree is empty'

def test_max_binary_search(my_tree):
    assert my_tree.max_binary_search() == 12

def test_max_binary_search_empty():
    tree = BinarySearchTree()
    assert tree.max_binary_search() == 'The tree is empty'


@pytest.fixture
def my_tree():
    tree = BinarySearchTree()
    [tree.insert(x) for x in [5,2,1,3,10,7,12]]
    return tree
