
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
        if type(new_value) is Node:
            return 'Please enter a value and it will converted to Node automaticly'
        else:
            new_node = Node(new_value)
        new_node.next = self.top
        self.top = new_node
    

    def pop(self):
        '''
        A method to remove a node from the stack
        Input: nothing
        '''
        if self.is_empty():
            return 'The stack is empty'
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

    def __str__(self):
        '''
        A method to print the stack
        Input: nothing
        Output: string
        '''
        output = ''
        if self.is_empty():
            return 'The stack is empty'
        else:
            current = self.top
            while current is not None:
                output += '{ ' f'{current.value}' ' } -> '
                current = current.next
            output += 'Null'
        return  output 



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
        A method to add a node to the queue (to the rear)
        Input: new value
        '''
        if type(new_value) is Node:
            return 'Please enter a value and it will converted to Node automaticly'
        else:
            new_node = Node(new_value)
        if not self.front:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node


    def dequeue(self):
        '''
        A method to remove a node from the queue (from front)
        Input: nothing
        '''
        if self.is_empty():
            return 'The queue is empty'
        else:
            current = self.front
            self.front = self.front.next
            current.next = None


    
    def peek(self):
        '''
        A method to show the front of the queue
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
        if self.front is None:
            return True
        else:
            return False

    def __str__(self):
        '''
        A method to print the queue
        Input: nothing
        Output: string
        '''
        output = ''
        if self.is_empty():
            return 'The queue is empty'
        else:
            current = self.front
            while current is not None:
                output += '{ ' f'{current.value}' ' } -> '
                current = current.next
            output += 'Null'
        return  output


class PseudoQueue():
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()
        self.front = None
        self.rear = None


    def enqueue(self, new_value):
        # enqueue to stack 1
        self.stack1.push(new_value)
        # dequeue from stack 1 and enqueue to stack 2
        if not self.stack2.is_empty():
            self.stack2 = Stack()
        current = self.stack1.top
        while current is not None:
            self.stack2.push(current.value)
            current = current.next
        
        self.convert_top_to_front_rear()


    def dequeue(self):
        if self.stack2.is_empty():
            return 'The queue is empty'
        current = self.stack2.top
        self.stack2.top = self.stack2.top.next
        current.next = None
        
        self.convert_top_to_front_rear()



    def is_empty(self):
        '''
        A method to check if the queue is empty or not
        Input: nothing
        Output: boolian (True if the queue is empty)
        '''
        if self.front is None:
            return True
        else:
            return False


    def convert_top_to_front_rear(self):
        self.front = self.stack2.top
        temp = self.stack2.top
        while temp is not None:
            self.rear = temp
            temp = temp.next


    def __str__(self):
        '''
        A method to print the queue
        Input: nothing
        Output: string
        '''
        output = ''
        if self.is_empty():
            return 'The queue is empty'
        else:
            current = self.front
            while current is not None:
                output += '{ ' f'{current.value}' ' } -> '
                current = current.next
            output += 'Null'
        return  output





if __name__ == '__main__':
    # Test the stack
    stack = Stack()
    print(stack.is_empty())
    stack.push('A')
    stack.push('B')
    stack.push('C')
    print(stack)
    stack.pop()
    print(stack)
    print(stack.peek())
    print(stack.is_empty())

    # Test the queue
    queue = Queue()
    print(queue.is_empty())
    queue.enqueue('A')
    queue.enqueue('B')
    queue.enqueue('C')
    print(queue)
    queue.dequeue()
    print(queue)
    print(queue.peek())
    print(queue.is_empty())

    # Test the pseudo queue
    pseudo_queue = PseudoQueue()
    pseudo_queue.enqueue('A')
    pseudo_queue.enqueue('B')
    pseudo_queue.enqueue('C')
    print(pseudo_queue)
    pseudo_queue.dequeue()
    print(pseudo_queue)