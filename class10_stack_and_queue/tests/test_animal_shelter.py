from class10_stack_and_queue.animal_shelter import AnimalShelter, Node
import pytest

def test_enqueue():
    shelter = AnimalShelter()
    shelter.enqueue('cat')
    shelter.enqueue('cat')
    shelter.enqueue('dog')
    actual = str(shelter)
    expected = '{ cat } -> { cat } -> { dog } -> Null'
    assert actual == expected

def test_enqueue_not_dog_cat():
    shelter = AnimalShelter()
    actual = shelter.enqueue('rabit')
    expected = 'We only receive dogs and cats'
    assert actual == expected

def test_enqueue_Node():
    shelter = AnimalShelter()
    actual = shelter.enqueue(Node('cat'))
    expected ='Please enter the animal type as a value (string) and it will converted to Node automaticly'
    assert actual == expected
    




def test_dequeue_front(my_shelter):
    actual = my_shelter.dequeue('cat')
    expected = 'cat'
    assert actual == expected
    assert str(my_shelter) == '{ dog } -> { dog } -> { dog } -> { cat } -> Null'

def test_dequeue_middle(my_shelter):
    actual = my_shelter.dequeue('dog')
    expected = 'dog'
    assert actual == expected
    assert str(my_shelter) == '{ cat } -> { dog } -> { dog } -> { cat } -> Null'

def test_dequeue_from_empty():
    shelter = AnimalShelter()
    actual = shelter.dequeue('cat')
    expected = 'The shelter queue is empty'
    assert actual == expected

def test_dequeue_not_dog_cat(my_shelter):
    shelter = AnimalShelter()
    actual = my_shelter.dequeue('rabit')
    expected = 'cat'
    assert actual == expected
    assert str(my_shelter) == '{ dog } -> { dog } -> { dog } -> { cat } -> Null'

def test_dequeue_no_argument(my_shelter):
    actual = my_shelter.dequeue()
    expected = 'cat'
    assert actual == expected
    assert str(my_shelter) == '{ dog } -> { dog } -> { dog } -> { cat } -> Null'


@pytest.fixture
def my_shelter():
    shelter = AnimalShelter()
    shelter.enqueue('cat')
    shelter.enqueue('dog')
    shelter.enqueue('dog')
    shelter.enqueue('dog')
    shelter.enqueue('cat')
    return shelter