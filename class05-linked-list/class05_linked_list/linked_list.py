
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

    def append(self, new_value):    # O(n)
        '''
        A method calls the class (Node) to create a node from the input value, then add that node to the end of the linked list. o(n)
        Input: new value (any type)
        '''
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def insert(self, new_value):      #O(1)
        '''
        A method calls the class (Node) to create a node from the input value, then add that node to the head of the linked list. O(1)
        Input: new value (any type)
        '''
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
        else:
            old_head = self.head
            self.head = new_node
            self.head.next = old_head

    def insert_before(self, value, new_value):
        '''
        A method calls the class (Node) to create a node from the input value, then add that node before a specific value in the linked list. O(n)
        Input: value , new_value (any type except boolean) 
        '''
        
        new_node = Node(new_value)
        if self.head is None:
            return 'The linked-list is empty'
        else:
            if self.head.value == value: # if you want to make a node with a boolean value use try except to handle errors insted of if statument
                self.insert(new_value)
                return
            current = self.head
            check = True
            while current is not None:
                if current.next is None:    # To avoid error when it trys to access the (next) attribute of the last node
                    break
                if current.next.value == value: # if you want to make a node with a boolean value use try except to handle errors insted of if statument
                    old_after = current.next
                    current.next = new_node
                    new_node.next = old_after
                    check = False
                    break
                current = current.next
            if check == True: 
                return 'This value is not exist in this linked list!'

    def insert_after(self, value, new_value):
        '''
        A method calls the class (Node) to create a node from the input value, then add that node after a specific value in the linked list. O(n)
        Input: value, new_value (any type except boolean)
        '''
        new_node = Node(new_value)
        if self.head is None:
            return 'The linked-list is empty'
        else:
            current = self.head
            check = True
            while current is not None:
                if current.value == value:    # if you want to make a node with a boolean value use try except to handle errors insted of if statument
                    old_after = current.next
                    current.next = new_node
                    new_node.next = old_after
                    check = False
                    break
                current = current.next
            if check == True:
                return 'This value is not exist in this linked list!'
                     

    def delete_node(self, value):
        '''
        A method to delete a node from the linked list. O(n)
        Input: the value of the node to delete (any type except boolean) 
        '''
        if self.head is None:
            return 'The linked-list is empty'
        else:
            if self.head.value == value:    # if you want to make a node with a boolean value use try except to handle errors insted of if statument
                self.head = self.head.next
                return
            current = self.head
            check = True
            while current is not None:
                if current.next is None:    # To avoid error when it trys to access the (next) attribute of the last node
                    break
                if current.next.value == value:   # if you want to make a node with a boolean value use try except to handle errors insted of if statument
                    current.next = current.next.next
                    check = False
                    break
                current = current.next
            if check == True:
                return 'This value is not exist in this linked list!'

    def includes(self, wanted_value):  #O(n)
        '''
        A method to search for search for a node's value in the linked list. O(n)
        Input: wanted_value (any type except boolean) 
        '''
        if self.head is None:
            return 'The linked-list is empty'
        else:
            output = False
            current = self.head
            while current is not None:
                if current.value == wanted_value:   # if you want to make a node with a boolean value use try except to handle errors insted of if statument
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
        A method calls the class (DNode) to create a node from the input value, then add that node to the head of the linked list. O(1)
        Input: new_value (any type except boolean)
        '''
        new_node = DNode(new_value)  
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
    # print(emad = Node('Emad'))     # exampile of a node

    ll.append('Emad')
    ll.append('Anas')
    ll.append('test')
    ll.insert(1)
    ll.insert('Yazan')
    ll.insert_after('Emad', 'after emad')
    ll.insert_before('Emad', 'before emad')
    ll.insert_before('Yazan', 'the head')
    ll.insert_before('test', 'the end')
    ll.delete_node('Emad')
    ll.delete_node('the head')
    ll.delete_node('test')

    # print(ll.append('not node HAHAHA'))


    # print(ll.delete_node('111'))
    # print(ll.insert_before('111', Node('the')))
    # print(ll.insert_after('111', Node('after')))


    print(ll)
    # print(ll.includes('Emad'))
    # print(ll.includes('An'))

    dll = DoublyLinkedList()
    dll.insert('this is an easy insert')
    # print(dll)
