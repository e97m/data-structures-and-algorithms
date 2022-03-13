from class05_linked_list.linked_list import Node, LinkedList, DNode, DoublyLinkedList
import pytest

def test_empty():
    actual = str(LinkedList())
    expected = 'The linked-list is empty'
    assert actual == expected

def test_insert_one():
    emad = Node('Emad')
    ll = LinkedList()
    ll.insert(emad)
    actual = str(ll)
    expected = '{ Emad } -> NULL'
    assert actual == expected

def test_insert_two():
    ll = LinkedList()
    ll.insert(Node('Emad'))
    ll.insert(Node('Anas'))
    actual = str(ll)
    expected = '{ Anas } -> { Emad } -> NULL'
    assert actual == expected

def test_includes_head(my_ll):
    actual = my_ll.includes('Yazan')
    expected = True
    assert actual == expected

def test_includes_mid(my_ll):
    actual = my_ll.includes('Anas')
    expected = True
    assert actual == expected

def test_includes_last(my_ll):
    actual = my_ll.includes('Emad')
    expected = True
    assert actual == expected

def test_includes_false(my_ll):
    actual = my_ll.includes('test')
    expected = False
    assert actual == expected

def test_dll_empty():
    actual = str(DoublyLinkedList())
    expected = 'The linked-list is empty'
    assert actual == expected

def test_dll_insert_one():
    dll = DoublyLinkedList()
    dll.insert('Emad')
    actual = str(dll)
    expected = '{ Emad } -> NULL'
    assert actual == expected

def test_dll_insert_two():
    dll = DoublyLinkedList()
    dll.insert('Emad')
    dll.insert('Anas')
    actual = str(dll)
    expected = '{ Anas } -> { Emad } -> NULL'
    assert actual == expected


@pytest.fixture
def my_ll():
    ll = LinkedList()
    ll.insert(Node('Emad'))
    ll.insert(Node('Anas'))
    ll.insert(Node('Yazan'))
    return ll
