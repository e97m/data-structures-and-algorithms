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
            self.table[idx] = [[key, value]]  # LinkedList().add({key, value})
        else:
            self.table[idx].append([key, value])

    def get(self, key):
        """
        A method to retrieve the vlaue of a key
        Input: key
        Output: value
        """
        return self.table[self.hash(key)]


# I have to use hash table
def tree_intersection(tree1, tree2):
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

    node1 = TNode(1)
    node2 = TNode(2)
    node3 = TNode(3)
    node4 = TNode(4)
    node1.left = node3
    node1.right = node2
    node3.left = node4
    tree = BinaryTree()
    tree.root = node1