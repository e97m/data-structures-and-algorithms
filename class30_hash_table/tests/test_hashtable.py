import pytest
from hash_table.hashtable import HashTable

def test_init():
    ht = HashTable()
    assert ht.size == 1024
    assert ht.table == [None] * 1024

def test_hash():
    ht = HashTable()
    assert ht.hash("bucket") == 858

def test_set():
    ht = HashTable()
    ht.set("bucket", "test")
    assert ht.table[ht.hash('bucket')] == [['bucket', 'test']]

def test_get(my_HT):
     assert my_HT.get("name") == [['name', 'Python']]

def test_get_collision(my_HT):
    assert my_HT.get("cloud") == [['cloud', 'AWS'], ['cloud', 'Azure'], ['could', 'Rainy']]

def test_get_null(my_HT):
    assert my_HT.get("random") == None

def test_keys(my_HT):
    assert my_HT.keys() == ['name', 'cloud']

def test_contains(my_HT):
    assert my_HT.contains("cloud") == True
    assert my_HT.contains("random") == False



@pytest.fixture
def my_HT():
    hashtable = HashTable()
    hashtable.set("cloud", "AWS")
    hashtable.set("cloud", "Azure")
    hashtable.set("could", "Rainy")
    hashtable.set("name", "Python")
    return hashtable