
import re


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
        # self.index = None


class LinkedList:
    '''
    A class to creat a singly linked list
    Input: no input
    constructor: head (the first node in the linked list)
    methods: append, insert, includes
    '''
    def __init__(self):
        self.head = None


    # def length(self):
    #     counter = 0
    #     current = self.head
    #     while current is not None:
    #         counter += 1
    #         current = current.next
    #     return counter

    def __len__(self):
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


    # def index(self):
    #     '''
    #     A method to (create/over write) an index for each node then append them to a list
    #     Input: nothing
    #     Output: list of indexes
    #     '''
    #     try:
    #         if self.head is None:
    #             raise ValueError
    #     except ValueError:
    #         return 'The linked-list is empty'
    #     else:
    #         list_of_index = []
    #         counter = 0
    #         current = self.head
    #         while current is not None:
    #             current.index = counter
    #             list_of_index.append(current.index)
    #             counter += 1
    #             current = current.next
    #     return list_of_index


    # def index_reversed(self):
    #     '''
    #     A method to (create/over write) a reversed index for each node then append them to a list
    #     Input: nothing
    #     Output: list of revered indexes
    #     '''
    #     try:
    #         if self.head is None:
    #             raise ValueError
    #     except ValueError:
    #         return 'The linked-list is empty'
    #     else:
    #         list_of_index = []
    #         counter = 1
    #         current = self.head
    #         while current is not None:
    #             current.index = len(self) - counter # __len__ is defined in this class
    #             list_of_index.append(current.index)
    #             counter += 1
    #             current = current.next
    #     return list_of_index


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
                    return 'This value does not exist in this linked list!'


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
                    return 'This value does not exist in this linked list!'
                     

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
                return 'This value does not exist in this linked list!'


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
            if self.head is None :
                raise ValueError
        except ValueError:
            return 'The linked-list is empty'
        else:
            length = len(self)
            try:
                if k > length or k < 0:
                    raise ValueError
            except ValueError:
                return 'Index not found!'
            else:
                current = self.head
                for _ in range(1, length - k):
                    current = current.next
                return current.value
            # old solution with index atribute
            # self.index_reversed()
            # current = self.head
            # while current is not None:
            #     if current.index == k:   
            #         return current.value
            #     current = current.next
            # return 'Index not found!'


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
            mid_element = (len(self)-1)//2
            current = self.head
            counter = 0
            while current is not None:
                if counter == mid_element:
                    return current.value
                counter += 1
                current = current.next
            # old solution with index atribute
            # self.index()
            # mid_index = (len(self)-1)//2

            # current = self.head
            # while current is not None:
            #     if current.index == mid_index:
            #         return current.value
            #     current = current.next


    # not tested in pytest
    def reverse(self):
        '''
        A method to reverse the linked list
        Input: nothing
        Output: reversed linked list
        '''
        try:
            if self.head is None:
                raise ValueError
        except ValueError:
            return 'The linked-list is empty'
        else:
            if self.head.next is None:
                return self.head.value
            else:
                counter =0
                length = len(self)
                if length == 0:
                    return 'The linked list is empty!'
                old_head = self.head
                for _ in range(length): 
                    current = old_head
                    for _ in range(length-1 - counter):
                        previous = current
                        current = current.next
                    if counter == 0:
                        self.head = current
                        self.head.next = previous
                    if counter == length -1:
                        current.next = None
                    else:
                        current.next = previous
                    counter += 1
            return self
    

    # not tested yet
    def palindrome(self, the_ll):
        '''
        A method to check if the linked list is symitric or not
        Input: a linked list
        Output: boolian (True if it is symitric)
        '''
        original_ll = the_ll
        revesed_ll = the_ll.reverse()
        original_current = original_ll.head
        reversed_current = revesed_ll.head
        while original_current is not None:
            if original_current.value != reversed_current.value:
                return False
            else:
                original_current = original_current.next
                reversed_current = reversed_current.next
        return True
                            
                          
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


def merge_liked_list(l_list_1, l_list_2):
    '''
    A function to merge two linked lists
    input: linked list 1, linked list 2
    ex: LL1 = A, B, C // LL2 = 1, 2, 3 ==> A, 1, B, 2, C, 3
    '''
    try:
        if not isinstance(l_list_1, LinkedList) or not isinstance(l_list_2, LinkedList):
            raise TypeError
    except TypeError:
        return 'Please make sure that the entered data type is LinkedList for both arguments'
    else:
        current1 = l_list_1.head
        current2 = l_list_2.head
        if l_list_1.head is None and l_list_2.head is not None:
            return l_list_2
        if l_list_2.head is None and l_list_1.head is not None:
            return l_list_1
        if l_list_1.head is None and l_list_2.head is None:
            return 'The linked-lists are empty'
        while current1 is not None or current2 is not None:
            new_next1 = current1.next
            current1.next = current2
            new_next2 = current2.next
            if new_next1 is None:
                current1 = new_next1
                current2= new_next2
                return l_list_1
            if new_next2 is None:
                current2.next = new_next1
                return l_list_1
            current2.next = new_next1
            current1 = new_next1
            current2= new_next2
        return l_list_1


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

    # print(ll.includes('Emad'))
    # print(ll.includes('An'))

    # print (ll.kth_from_end(10))

    print(ll)
    print(len(ll))
    print(ll.reverse())

    # dll = DoublyLinkedList()
    # dll.insert('this is an easy insert')

    
    # print(dll)
    # print(ll.find_mid())

    my_l_list_1 = LinkedList()
    # my_l_list_1.insert('D')
    # my_l_list_1.insert('C')
    my_l_list_1.insert('B')
    my_l_list_1.insert('A')

    my_l_list_2 = LinkedList()
    my_l_list_2.insert('4')
    my_l_list_2.insert('3')
    my_l_list_2.insert('2')
    my_l_list_2.insert('1')

    print(merge_liked_list(my_l_list_1, my_l_list_2))