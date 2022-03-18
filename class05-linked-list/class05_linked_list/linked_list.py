
class Node:
    '''
    A class to creat a node to be used in singly linked list
    Input: the value of the data for the node.
    constructor: vlaue, next (pointer to the next), index
    methods: no methods
    '''
    def __init__(self,value):
        self.value = value
        self.next = None
        self.index = None


class LinkedList:
    '''
    A class to creat a singly linked list
    Input: no input
    constructor: head (the first node in the linked list)
    methods: append, insert, includes
    '''
    def __init__(self):
        self.head = None


    def length(self):
        '''
        A method to canculate the length of the linked list
        Input: nothing
        Output: length(int)
        '''
        counter = 0
        current = self.head
        while current is not None:
            counter += 1
            current = current.next
        return counter


    def index(self):
        '''
        A method to (create/over write) an index for each node then append them to a list
        Input: nothing
        Output: list of indexes
        '''
        try:
            if self.head is None:
                raise ValueError
        except ValueError:
            return 'The linked-list is empty'
        else:
            list_of_index = []
            counter = 0
            current = self.head
            while current is not None:
                current.index = counter
                list_of_index.append(current.index)
                counter += 1
                current = current.next
        return list_of_index


    def index_reversed(self):
        '''
        A method to (create/over write) a reversed index for each node then append them to a list
        Input: nothing
        Output: list of revered indexes
        '''
        try:
            if self.head is None:
                raise ValueError
        except ValueError:
            return 'The linked-list is empty'
        else:
            length = self.length()
            list_of_index = []
            counter = 1
            current = self.head
            while current is not None:
                current.index = length - counter
                list_of_index.append(current.index)
                counter += 1
                current = current.next
        return list_of_index


    def append(self, new_value):    # O(n)
        '''
        A method calls the class (Node) to create a node from the input value, then add that node to the end of the linked list. o(n)
        Input: new value (any type)
        '''
        try:
            if isinstance(new_value, Node):
                raise TypeError
        except TypeError:
            return 'please enter a value, it will be converted to Node automaticly'
        else:
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
        try:
            if isinstance(new_value, Node):
                raise TypeError
        except TypeError:
            return 'please enter a value, it will be converted to Node automaticly'
        else:
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
        Input: value , new_value (any type) 
        '''
        try:
            if isinstance(new_value, Node):
                raise TypeError
        except TypeError:
            return 'please enter a value, it will be converted to Node automaticly'
        else:
            new_node = Node(new_value)

            try:
                if self.head is None:
                    raise ValueError
            except ValueError:
                return 'The linked-list is empty'
            else:
                if self.head.value == value:
                    self.insert(new_value)
                    return
                current = self.head
                check = True
                while current is not None:
                    if current.next is None:    # This to avoid error when it trys to access the (next) attribute of the last node
                        break
                    if current.next.value == value:
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
        Input: value, new_value (any type)
        '''
        try:
            if isinstance(new_value, Node):
                raise TypeError
        except TypeError:
            return 'please enter a value, it will be converted to Node automaticly'
        else:
            new_node = Node(new_value)
            
            try:
                if self.head is None:
                    raise ValueError
            except ValueError:
                return 'The linked-list is empty'
            else:
                current = self.head
                check = True
                while current is not None:
                    if current.value == value:
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
        Input: the value of the node to delete (any type) 
        '''
        try:
            if self.head is None:
                raise ValueError
        except ValueError:
            return 'The linked-list is empty'
        else:
            if self.head.value == value:
                self.head = self.head.next
                return

            current = self.head
            check = True
            while current is not None:
                if current.next is None:    # This to avoid error when it trys to access the (next) attribute of the last node
                    break
                if current.next.value == value:
                    current.next = current.next.next
                    check = False
                    break
                current = current.next
            if check == True:
                return 'This value is not exist in this linked list!'


    def includes(self, wanted_value):  #O(n)
        '''
        A method to search for search for a node's value in the linked list. O(n)
        Input: wanted_value (any type) 
        '''
        try:
            if self.head is None:
                raise ValueError
        except ValueError:
            return 'The linked-list is empty'
        else:
            current = self.head
            while current is not None:
                if current.value == wanted_value:
                    return True
                current = current.next
            return False


    def kth_from_end(self, k):
        '''
        A method to return the value of an index from the tail of the linked list
        Input: kth position from the tail (int)
        Output: the value of the wanted index
        '''
        try:
            if self.head is None:
                raise ValueError
        except ValueError:
            return 'The linked-list is empty'
        else:
            self.index_reversed()
            current = self.head
            while current is not None:
                if current.index == k:   
                    return current.value
                current = current.next
            return 'Index not found!'


    def find_mid(self):
        '''
        A method to find the middle node in the linked list
        Input: nothing
        Outpu: the value of the middle node
        '''
        try:
            if self.head is None:
                raise ValueError
        except ValueError:
            return 'The linked-list is empty'
        else:
            length = self.length()
            self.index()
            mid_index = (length-1)//2

            current = self.head
            while current is not None:
                if current.index == mid_index:
                    return current.value
                current = current.next


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
        Input: new_value (any type)
        '''
        try:
            if isinstance(new_value, DNode):
                raise TypeError
        except TypeError:
            return 'please enter a value, it will be converted to (DNode) node automaticly'
        else:
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
    emad = "Emad"

    ll.append(emad)
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
    ll.insert_before('Yazan', True)
    ll.delete_node(True)


    # print(ll.insert( Node('ttttttttttttt')))
    # print(ll.append(Node('node HAHAHA')))

    # print(ll.delete_node('111'))
    # print(ll.insert_before('111', Node('the')))
    # print(ll.insert_after('111', 'after'))

    print(ll)

    # print(ll.includes('Emad'))
    # print(ll.includes('An'))

    # dll = DoublyLinkedList()
    # dll.insert('this is an easy insert')
    # print(dll)

    # print (ll.kth_from_end(10))
    print(ll.find_mid())