class Node:
  def __init__(self, value):
    self.value = value
    self.next = None


class Stack:
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
        return current.value
    

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
    
    def peek(self):
        '''
        A method to show the top of the stack
        '''
        if self.is_empty():
            return 'The stack is empty'
        else:
            return self.top.value
      

class TNode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right=None


class BinaryTree:

    def __init__(self):
        self.root = None
    

    def pre_order_recursive(self):
        """
        A method to traverse a tree in pre-order
        Input: None
        output: print the value of each node
        """
        current = self.root
        if current is None: return 'The tree is empty'
        values = []

        def _walk(current):
            values.append(current.value)
            if current.left:
                _walk(current.left)
            if current.right:
                _walk(current.right)

        _walk(current)
        return values


    def in_order_recursive(self):
        """
        A method to traverse a tree in pre-order
        Input: None
        output: print the value of each node
        """
        current = self.root
        if current is None: return 'The tree is empty'
        values = []

        def _walk(current):
            if current.left:
                _walk(current.left)
            values.append(current.value)
            if current.right:
                _walk(current.right)

        _walk(current)
        return values


    def post_order_recursive(self):
        """
        A method to traverse a tree in pre-order
        Input: None
        output: print the value of each node
        """
        current = self.root
        if current is None: return 'The tree is empty'
        values = []

        def _walk(current):
            if current.left:
                _walk(current.left)
            if current.right:
                _walk(current.right)
            values.append(current.value)

        _walk(current)
        return values


    def pre_order(self):
        """
        A method to traverse the tree elements in pre-order
        input: None
        output: print a list of the value of each node
        """
        current = self.root
        if current is None: return 'The tree is empty'
        values = []
        stack = Stack()
        stack.push(current)
        while not stack.is_empty():
            current = stack.pop()
            values.append(current.value)
            if current.right:
                stack.push(current.right)
            if current.left:
                stack.push(current.left)
        return values
    

    def in_order(self):
        """
        A method to traverse the tree elements in in-order
        input: None
        output: print a list of  the value of each node
        """
        current = self.root
        if current is None: return 'The tree is empty'
        values = []
        stack = Stack()
        while True:
            if current is not None:
                stack.push(current)
                current = current.left
            elif not stack.is_empty():
                current = stack.pop()
                values.append(current.value)
                current = current.right
            else:
                break
        return values

    
    def post_order(self):
        """
        A method to traverse the tree elements in post-order
        input: None
        output: print a list of  the value of each node
        """
        current = self.root
        if current is None: return 'The tree is empty'
        values = []
        stack = Stack()  
        while True:
            while current is not None:
                if current.right is not None:
                    stack.push(current.right)
                stack.push(current)
                current = current.left
            current = stack.pop()
            if current.right is not None and stack.peek() == current.right:
                stack.pop()
                stack.push(current)
                current = current.right
            else:
                values.append(current.value)
                current = None
            if stack.is_empty():
                break
        return values


class BinarySearchTree(BinaryTree):
    def __init__(self):
        super().__init__()
    

    def insert(self, new_value):
        """
        A method to insert a node to the tree
        input: value
        output: None
        """
        if type(new_value) is TNode or type(new_value) is Node or type(new_value) is KNode:
            return 'Please enter a value, it will be converted automaticly to TNode'
        if self.root is None:
            self.root = TNode(new_value)
        else:
            current = self.root
            while True:
                if new_value < current.value:
                    if current.left is None:
                        current.left = TNode(new_value)
                        break
                    else:
                        current = current.left
                elif new_value > current.value:
                    if current.right is None:
                        current.right = TNode(new_value)
                        break
                    else:
                        current = current.right
                else:
                    break
    

    def find(self, value):
        """
        A method to find a node in the tree
        input: value
        output: True if the node is in the tree, False if not
        """
        current = self.root
        if current is None: return 'The tree is empty'
        while current:
            if value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right
            else:
                return True
        return False
    

# Not working yet, this isn't a task nor a strech goal
    def delete(self, value):
        """
        A method to delete a node in the tree
        input: value
        output: True if the node is in the tree, False if not
        """
        if self.root is None:
            return 'The tree is empty'
        else:
            current = self.root
            parent = None
            while current:
                if value < current.value:
                    parent = current
                    current = current.left
                elif value > current.value:
                    parent = current
                    current = current.right
                else:
                    if current.left is None and current.right is None:
                        if parent.left == current:
                            parent.left = None
                        else:
                            parent.right = None
                    elif current.left is None:
                        if parent.left == current:
                            parent.left = None
                        elif parent.right == current:
                            parent.right = current.right
                    elif current.right is None:
                        if parent.left == current:
                            parent.left = current.left
                        elif parent.right == current:
                            parent.right = None








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

# strech goal
class KNode:
    def __init__(self, value):
        self.value = value
        self.children = []
                 
# strech goal
class KAryTree:
    def __init__(self):
        self.root = None


    def breadthFirst(self):
        '''
        A method to traverse the k-ary-tree elements (breadthFirst)
        input: None
        output: print a list of the value of each node
        '''
        current = self.root
        if current is None: return 'The tree is empty'
        values = []
        queue = Queue()
        queue.enqueue(current)
        while not queue.is_empty():
            current = queue.dequeue()
            values.append(current.value)
            for child in current.children:
                queue.enqueue(child)
        return values
        

    # strech goal, not compleated
    def insert_k(self, new_value, parent_value):
        '''
        A method to create a KNode and insert it under a given parent node
        input: new vlaue, parent value
        output: None
        '''
        if type(new_value) is TNode or type(new_value) is Node or type(new_value) is KNode:
            return 'Please enter a value, it will be converted automaticly to TNode'
        if self.root is None:
            self.root = KNode(new_value)
        else:
            pass
           
            

        



if __name__ == '__main__':

    # node1 = TNode(1)
    # node2 = TNode(2)
    # node3 = TNode(3)
    # node4 = TNode(4)
    # node1.left = node2
    # node1.right = node3
    # node3.right = node4
    # tree = BinaryTree()
    # tree.root = node1
    # tree.pre_order()

    tree2 = BinarySearchTree()
    tree2.insert(5)
    tree2.insert(2)
    tree2.insert(1)
    tree2.insert(3)
    tree2.insert(10)
    tree2.insert(7)
    tree2.insert(12)
    # tree2.delete(2)

    print(tree2.pre_order())
    print(tree2.pre_order_recursive())
    print(tree2.find(10))
    print(tree2.in_order())
    print(tree2.in_order_recursive())
    print(tree2.find(15))
    print(tree2.post_order())
    print(tree2.post_order_recursive())

    print('K Ary Tree')

    tree3 = KAryTree()
    tree3.root = KNode(5)
    tree3.root.children = KNode(3), KNode(2), KNode(4)
    tree3.root.children[0].children = KNode(1), KNode(0)
    tree3.root.children[2].children = KNode(6), KNode(7)
    # tree3.insert_k(5, None)
    # tree3.insert_k(2, 5)
    # tree3.insert_k(10, 5)
    # tree3.insert_k(1, 5)
    # tree3.insert_k(1, 2)
    # tree3.insert_k(3, 2)
    # tree3.insert_k(4, 2)
    # tree3.insert_k(7, 10)
    # tree3.insert_k(12, 10)
    # tree3.insert_k(12, 15)


    print(tree3.breadthFirst())

