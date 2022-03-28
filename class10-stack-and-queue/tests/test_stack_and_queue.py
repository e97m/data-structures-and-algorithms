
from class10_stack_and_queue.stack_and_queue import Node, Stack, Queue, PseudoQueue
import pytest

def test_push():
    stack = Stack()
    stack.push('A')
    actual = str(stack)
    expected = '{ A } -> Null'
    assert actual == expected

def test_push_2():
    stack = Stack()
    stack.push('A')
    stack.push('B')
    actual = str(stack)
    expected = '{ B } -> { A } -> Null'
    assert actual == expected

def test_pop(my_stack):
    my_stack.pop()
    actual = str(my_stack)
    expected = '{ B } -> { A } -> Null'
    assert actual == expected
    
def test_pop_2():
    stack = Stack()
    stack.push('A')
    stack.pop()
    actual = str(stack)
    expected = 'The stack is empty'
    assert actual == expected

def test_pop_3():
    stack = Stack()
    stack.pop()
    actual = str(stack)
    expected = 'The stack is empty'
    assert actual == expected

def test_peek(my_stack):
    actual = my_stack.peek()
    expected = 'C'
    assert actual == expected

def test_stack_is_empty():
    stack = Stack()
    actual = stack.is_empty()
    expected = True
    assert actual == expected

def test_stack_is_empty_2(my_stack):
    actual = my_stack.is_empty()
    expected = False
    assert actual == expected

def test_enqueue():
    queue = Queue()
    queue.enqueue('A')
    actual = str(queue)
    expected = '{ A } -> Null'
    assert actual == expected

def test_enqueue_2():
    my_queue = Queue()
    my_queue.enqueue('A')
    my_queue.enqueue('B')
    actual = str(my_queue)
    expected = '{ A } -> { B } -> Null'
    assert actual == expected

def test_dequeue(my_queue):
    my_queue.dequeue()
    actual = str(my_queue)
    expected = '{ B } -> { C } -> Null'
    assert actual == expected

def test_dequeue_2():
    my_queue = Queue()
    my_queue.enqueue('A')
    my_queue.dequeue()
    actual = str(my_queue)
    expected = 'The queue is empty'
    assert actual == expected

def test_dequeue_3():
    my_queue = Queue()
    my_queue.dequeue()
    actual = str(my_queue)
    expected = 'The queue is empty'
    assert actual == expected

def test_queue_peek(my_queue):
    actual = my_queue.peek()
    expected = 'A'
    assert actual == expected

def test_queue_is_empty(my_queue):
    actual = my_queue.is_empty()
    expected = False
    assert actual == expected

def test_queue_is_empty_2():
    my_queue = Queue()
    actual = my_queue.is_empty()
    expected = True
    assert actual == expected

def test_pseudo_queue_enqueue():
    pseudo_queue = PseudoQueue()
    pseudo_queue.enqueue('A')
    actual = str(pseudo_queue)
    expected = '{ A } -> Null'
    assert actual == expected

def test_pseudo_queue_enqueue_2():
    pseudo_queue = PseudoQueue()
    pseudo_queue.enqueue('A')
    pseudo_queue.enqueue('B')
    pseudo_queue.enqueue('C')
    actual = str(pseudo_queue)
    expected = '{ A } -> { B } -> { C } -> Null'
    assert actual == expected

def test_pseudo_queue_dequeue(my_pseudo_queue):
    my_pseudo_queue.dequeue()
    actual = str(my_pseudo_queue)
    expected = '{ B } -> { C } -> Null'
    assert actual == expected

def test_pseudo_queue_dequeue_2():
    my_pseudo_queue = PseudoQueue()
    my_pseudo_queue.dequeue()
    actual = str(my_pseudo_queue)
    expected = 'The queue is empty'
    assert actual == expected

def test_pseudo_queue_dequeue_3():
    my_pseudo_queue = PseudoQueue()
    my_pseudo_queue.enqueue('A')
    my_pseudo_queue.dequeue()
    actual = str(my_pseudo_queue)
    expected = 'The queue is empty'
    assert actual == expected


@pytest.fixture
def my_stack():
    stack = Stack()
    stack.push('A')
    stack.push('B')
    stack.push('C')
    return stack

@pytest.fixture
def my_queue():
    queue = Queue()
    queue.enqueue('A')
    queue.enqueue('B')
    queue.enqueue('C')
    return queue

@pytest.fixture
def my_pseudo_queue():
    pseudo_queue = PseudoQueue()
    pseudo_queue.enqueue('A')
    pseudo_queue.enqueue('B')
    pseudo_queue.enqueue('C')
    return pseudo_queue