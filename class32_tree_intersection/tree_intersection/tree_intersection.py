class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

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


class BinarySearchTree(BinaryTree):
    def __init__(self):
        super().__init__()
    

    def insert(self, new_value):
        """
        A method to insert a node to the tree
        input: value
        output: None
        """
        if type(new_value) is TNode or type(new_value) is Node:
            return 'Please enter a value, it will be converted automaticly to TNode'
        if self.root is None:
            self.root = TNode(new_value)
        else:
            current = self.root
            while True:
                if new_value == current.value: return 'value is already exist'
                elif new_value < current.value:
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




class HashTable(object):
    def __init__(self, size=1024):
        self.size = size
        self.table = [None] * size
        # self.table = [LinkedList()]*size

    def hash(self, key):
        """
        A method to hash the key according to ASCII size
        Input: key
        Output: hash value
        """
        key = str(key)
        sum_of_ascii = 0
        for ch in key:
            ch_ascii = ord(ch)  # 86
            sum_of_ascii += ch_ascii
        hashed_key = (sum_of_ascii * 19) % self.size
        return hashed_key

    def set(self, key, value):
        """
        A method to hash the key, then set the key and value pair in the table, handling collisions as needed
        Input: key, value
        Output: othing
        """
        idx = self.hash(key)
        if not self.table[idx]:
            self.table[idx] = [[key, value]]  # LinkedList().insert({key, value})
        else:
            self.table[idx].append([key, value])

    def get(self, key):
        """
        A method to retrieve the vlaue of a key
        Input: key
        Output: value
        """
        return self.table[self.hash(key)]

    def contains(self, key):
        """
        A method to check if the key is already in the hash table
        Input: key
        Output: boolean
        """
        if self.get(key) is not None:
            return True
        else:
            return False


def tree_intersection(tree1, tree2):
    '''
    A function to append to an array the intersection values of two binary trees.
    Input: two trees
    Output: arr of common values
    '''
    ht = HashTable()
    arr1 = tree1.pre_order_recursive()
    arr2 = tree2.pre_order_recursive()
    if len(arr1) == '' or len(arr2) == '':
        return 'One or both trees is empty'
    output = []
    for i in arr1:
        ht.set(i, 1)
    for i in arr2:
        if ht.contains(i):
            output.append(i)
    return output


def tree_intersection_arr(tree1, tree2):
    '''
    A function to append to an array the intersection values of two binary trees.
    Input: two trees
    Output: arr of common values
    '''
    arr1 = tree1.pre_order_recursive()
    arr2 = tree2.pre_order_recursive()
    arr3 = []
    for i in arr1:
        if i in arr2:
            arr3.append(i)
    return arr3



if __name__ == '__main__':

    tree1 = BinarySearchTree()
    tree1.insert(5)
    tree1.insert(3)
    tree1.insert(7)
    tree1.insert(2)
    tree1.insert(4)
    tree1.insert(6)
    tree1.insert(8)

    tree2 = BinarySearchTree()
    tree2.insert(3)
    tree2.insert(5)
    tree2.insert(6)
    tree2.insert(7)
    tree2.insert(8)

    print(tree_intersection(tree1, tree2))