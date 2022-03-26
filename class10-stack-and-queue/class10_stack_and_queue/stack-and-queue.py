
class Node:
    '''
    A class to create a node
    Input: the value of the data for the node.
    constructor: vlaue, next (pointer to the next)
    '''
    def __init__(self,value):
        self.value = value
        self.next = None


class Stack:
    '''
    A class to creat a stack
    Input: no input
    constructor: top node
    '''

    def __init__(self):
        self.top = None


    def push(self, new_value):
        '''
        A method to add a node to the stack
        Input: new_value
        '''
        new_node = Node(new_value)
        new_node.top = self.top
        self.top = new_node
    

    def pop(self):
        '''
        A method to remove a node from the stack
        Input: nothing
        '''
        current = self.top
        self.top = self.top.next
        current.next = None


    def peek(self):
        '''
        A method to show the top of the stack
        '''
        if self.is_empty():
            return 'The stack is empty'
        else:
            return self.top.value
    

    def is_empty(self):
        '''
        A method to check if the stack is empty or not
        Input: nothing
        Output: boolian (True if the stack is empty)
        '''
        if self.top is None:
            return True
        else:
            return False


class Queue:
    '''
    A class to creat a queue
    Input: no input
    constructor: front node, rear node
    '''

    def __init__(self):
        self.front = None
        self.rear = None

    
    def enqueue(self, new_value):
        '''
        A method to add a node to the queue
        Input: new value
        '''
        new_node = Node(new_value)
        if not self.front:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node


    def dequeue(seld):
        '''
        A method to remove a node from the queue
        Input: nothing
        '''
        

    
    def peek(self):
        '''
        A method to show the top of the queue
        '''
        if self.is_empty():
            return 'The queue is empty'
        else:
            return self.front.value
    

    def is_empty(self):
        '''
        A method to check if the queue is empty or not
        Input: nothing
        Output: boolian (True if the queue is empty)
        '''
        if self.rear is None:
            return True
        else:
            return False