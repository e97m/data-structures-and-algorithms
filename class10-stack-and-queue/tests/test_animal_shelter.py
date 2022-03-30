from class10_stack_and_queue.animal_shelter import AnimalShelter
import pytest

def test_add_animal():
    shelter = AnimalShelter()
    shelter.add_animal('cat')
    shelter.add_animal('cat')
    shelter.add_animal('dog')
    actual = str(shelter.cats_queue)
    expected = '{ cat } -> { cat } -> Null'
    assert actual == expected
    actual2 = str(shelter.dogs_queue)
    expected2 = '{ dog } -> Null'
    assert actual2 == expected2

def test_add_animal_not_dog_cat():
    shelter = AnimalShelter()
    actual = shelter.add_animal('rabit')
    expected = 'We only receive dogs and cats'
    assert actual == expected

def test_add_animal_cat1():
    shelter = AnimalShelter()
    shelter.add_animal('cat')
    actual = str(shelter.cats_queue)
    expected = '{ cat } -> Null'
    assert actual == expected
    actual2 = str(shelter.dogs_queue)
    expected2 = 'The shelter queue for this animal type is empty'
    assert actual2 == expected2

def test_add_animal_dog1():
    shelter = AnimalShelter()
    shelter.add_animal('dog')
    actual = str(shelter.dogs_queue)
    expected = '{ dog } -> Null'
    assert actual == expected
    actual2 = str(shelter.cats_queue)
    expected2 = 'The shelter queue for this animal type is empty'
    assert actual2 == expected2

def test_request_animal(my_shelter):
    actual = my_shelter.request_animal('cat')
    expected = 'cat'
    assert actual == expected
    actual2 = my_shelter.request_animal('dog')
    expected2 = 'dog'
    assert actual2 == expected2

def test_request_animal_from_empty():
    shelter = AnimalShelter()
    actual = shelter.request_animal('cat')
    expected = 'The shelter queue for this animal type is empty'
    assert actual == expected
    actual2 = shelter.request_animal('dog')
    expected2 = 'The shelter queue for this animal type is empty'
    assert actual2 == expected2

def test_request_animal_not_dog_cat():
    shelter = AnimalShelter()
    actual = shelter.request_animal('rabit')
    expected = 'We only have dogs and cats'
    assert actual == expected

def test_request_animal_no_argument(my_shelter):
    actual = my_shelter.request_animal()
    expected = 'Please enter the animal type as a value (string)'
    assert actual == expected


@pytest.fixture
def my_shelter():
    shelter = AnimalShelter()
    shelter.add_animal('cat')
    shelter.add_animal('dog')
    shelter.add_animal('dog')
    shelter.add_animal('dog')
    shelter.add_animal('cat')
    return shelter