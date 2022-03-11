

class Node:
    '''
    A class to creat a node to be used in singly linked list
    Input: the value of the data for the node.
    constructor: vlaue, next (pointer to the next)
    methods: no methods
    '''
    def __init__(self,value):
        self.value = value
        self.next = None


class LinkedList:
    '''
    A class to creat a singly linked list
    Input: no input
    constructor: head (the first node in the linked list)
    methods: append, insert, includes
    '''
    def __init__(self):
        self.head = None

    def append(self, new_node):    # O(n)
        '''
        A method to add a node to the end of the linked list. o(n)
        Input: new node (not new value, you need to creat the node from its own class then add the node here)
        '''
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def insert(self, new_node):      #O(1)
        '''
        A method to add a node to the head of the linked list. O(1)
        Input: new node (not new value, you need to creat the node from its own class then add the node here)
        '''
        if self.head is None:
            self.head = new_node
        else:
            old_head = self.head
            self.head = new_node
            self.head.next = old_head

    def includes(self, wanted_value):  #O(n)
        '''
        A method to search for search for a node's value in the linked list. O(n)
        Input: wanted value
        '''
        if self.head is None:
            return 'The linked-list is empty'
        else:
            output = False
            current = self.head
            while current is not None:
                if current.value == wanted_value:
                    output = True
                current = current.next
            return output

    def __str__(self):
        output = ''
        if self.head is None:
            output += 'The linked-list is empty'
        else:
            current = self.head
            while current is not None:
                output += '{ ' f'{current.value}' ' } -> '
                current = current.next
            output += 'NULL'
        return  output 


class DNode:
    '''
    A class to creat a node to be used in doubly linked list
    Input: the value of the data for the node.
    constructor: vlaue, next (pointer to the next), prev (pointer to the previous)
    methods: no methods
    '''
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    '''
    A class to creat a doubly linked list
    Input: no input
    constructor: head (the first node in the linked list)
    methods: insert
    '''
    def __init__(self):
        self.head = None

    def insert(self,new_value):
        '''
        A method to add a node to the head of the linked list. O(1)
        Input: new value (any type)
        '''
        new_node = Node(new_value)  #this make the insert faster by inputing the value dirictly insted of add the value to the node then add the node here
        new_node.next = self.head
        if self.head is not None:
             self.head.prev = new_node
        self.head = new_node


    def __str__(self):
        output = ''
        if self.head is None:
            output += 'The linked-list is empty'
        else:
            current = self.head
            while current is not None:
                output += '{ ' f'{current.value}' ' } -> '
                current = current.next
            output += 'NULL'
        return  output 




if __name__ == '__main__':
    ll = LinkedList()
    emad = Node('Emad')     #node 1
    anas = Node('Anas')     #node 2
    yazan = Node('Yazan')   #node 3
    ll.append(emad)
    ll.append(Node(True))
    ll.insert(Node(1))
    ll.insert(Node('test'))

    print(ll)
    print(ll.includes('Emad'))
    print(ll.includes('An'))

    dll = DoublyLinkedList()
    dll.insert('this is an easy insert')
    print(dll)
