

class Node:

    def __init__(self,value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_node):    # O(n)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def insert(self, new_node):      #O(1)
        if self.head is None:
            self.head = new_node
        else:
            old_head = self.head
            self.head = new_node
            self.head.next = old_head

    def includes(self, data):
        if self.head is None:
            return 'The linked-list is empty'
        else:
            output = False
            current = self.head
            while current is not None:
                if current.value == data:
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
