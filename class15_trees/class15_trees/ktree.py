class Node:
  def __init__(self, value):
    self.value = value
    self.next = None


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
        return current.value


    
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

class KNode:
    def __init__(self, value):
        self.value = value
        self.children = []
                 
class KAryTree:
    '''A class to manipulate the K-Ary-Tree'''
    def __init__(self):
        self.root = None


    def breadth_first_k(self):
        '''
        A method to traverse the k-ary-tree elements (breadthFirst)
        input: tree
        output: print a list of the value of each node
        '''
        if not isinstance(self, KAryTree):
            raise Exception ('Please enter a KAryTree')
        current = self.root
        if current is None: raise Exception('The tree is empty')
        values = []
        queue = Queue()
        queue.enqueue(current)
        while not queue.is_empty():
            current = queue.dequeue()
            values.append(current.value)
            for child in current.children:
                queue.enqueue(child)
        return values   
        

    # not compleated
    def insert_k(self, new_value, k):
        '''
        A method to create a KNode and insert it under a given parent node
        input: new vlaue, maximum number of children
        output: None
        '''
        if type(new_value) is Node or type(new_value) is KNode:
            return 'Please enter a value, it will be converted automaticly to TNode'
        if self.root is None:
            self.root = KNode(new_value)
        else:
            current = self.root
            if len(current.children) < k:
                current.children.append(KNode(new_value))
            else:
                for i in range(1000):
                    if len(current.children[i].children) < k:
                        current = current.children[i]
                        current.children.append(KNode(new_value))
                        break     

        # not compleated
    def  fizz_buzz_tree(self):
        '''
        A method to traverse the k-ary-tree elements (breadthFirst) then return a tree has the value:
            Fizz if it divisible by 3
            Buzz if it divisible by 5
            FizzBuzz if it divisible by 3 and 5
        input: k_tree
        output: FizzBuzz K-tree
        '''
        if not isinstance(self, KAryTree):
            raise Exception ('Please enter a KAryTree')
        current = self.root
        if current is None: raise Exception('The tree is empty')
        value = []
        queue = Queue()
        queue.enqueue(current)
        while not queue.is_empty():
            current = queue.dequeue()
            if current.value %3 == 0 and current.value %5 ==0:
                value.append('FizzBuzz')
            elif current.value %3 == 0:
                value.append('Fizz')
            elif current.value %5 == 0:
                value.append('Buzz')
            else:
                value.append(f'{current.value}')

            max_k = len(self.root.children)
            for child in current.children:
                if len(current.children) > max_k:
                    max_k = len(current.children)
                queue.enqueue(child)

        count = 1
        new_k_ary_tree = KAryTree()
        for i in value:
            if count == 1:
                new_k_ary_tree.insert_k(i, 1)
            else:
                new_k_ary_tree.insert_k(i, max_k)
            count += 1 
        return new_k_ary_tree



if __name__ == '__main__':

    tree = KAryTree()
    tree.root = KNode(5)
    tree.root.children = KNode(3), KNode(2), KNode(4)
    tree.root.children[0].children = KNode(1), KNode(0)
    tree.root.children[2].children = KNode(6), KNode(15)

    print('tree: ',tree.breadth_first_k())

    tree2 = KAryTree()
    k2=3
    tree2.insert_k(5, 1)
    tree2.insert_k(2, k2)
    tree2.insert_k(10, k2)
    tree2.insert_k(1, k2)
    tree2.insert_k(1, k2)
    tree2.insert_k(3, k2)
    tree2.insert_k(4, k2)
    tree2.insert_k(7, k2)
    tree2.insert_k(12, k2)
    tree2.insert_k(15, k2)

    print('tree2:',tree2.breadth_first_k())
    print('fizzbuzz:',tree2.fizz_buzz_tree().breadth_first_k())



