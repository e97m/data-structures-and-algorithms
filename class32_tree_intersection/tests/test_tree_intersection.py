from tree_intersection import __version__
import pytest
from tree_intersection.tree_intersection import *


def test_version():
    assert __version__ == '0.1.0'


def test_tree_intersection(tree1, tree2):
    assert tree_intersection(tree1, tree2) == [3, 5, 6, 7, 8]


def test_tree_intersection_one_empty(tree1):
    tree2 = BinarySearchTree()
    with pytest.raises(Exception):
        assert tree_intersection(tree1, tree2)

def test_tree_intersection_two_empty():
    tree1 = BinarySearchTree()
    tree2 = BinarySearchTree()
    with pytest.raises(Exception):
        assert tree_intersection(tree1, tree2)


@pytest.fixture
def tree1():
    tree1 = BinarySearchTree()
    tree1.insert(5)
    tree1.insert(3)
    tree1.insert(7)
    tree1.insert(2)
    tree1.insert(4)
    tree1.insert(6)
    tree1.insert(8)
    return tree1

@pytest.fixture
def tree2():
    tree2 = BinarySearchTree()
    tree2.insert(3)
    tree2.insert(5)
    tree2.insert(6)
    tree2.insert(7)
    tree2.insert(8)
    return tree2