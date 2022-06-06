from class15_trees.class15_trees.tree import *

class NewBST(BinarySearchTree):
    def __init__(self):
        super().__init__()

    def get_successor(self, value):
        """
        A method to find the successor of a node in the tree (smallest value that is greater than the value)
        input: value
        output: successor value
        """
        if self.root is None:
            raise ValueError("The tree is empty")
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
                if current.right:
                    current = current.right
                    while current.left :
                        current = current.left
                    return current.value
                else:
                    return parent.value


if __name__ == '__main__':
    BST = NewBST()
    BST.insert(41)
    BST.insert(5)
    BST.insert(6)
    BST.insert(20)
    BST.insert(22)
    BST.insert(25)
    BST.insert(47)
    BST.insert(58)
    BST.insert(60)
    BST.insert(69)
    BST.insert(74)
    BST.insert(96)
    BST.insert(92)
    BST.insert(84)

    print(BST.get_successor(25))
    print(BST.get_successor(41))

    print(BST.get_predecessor(74))
    print(BST.get_predecessor(47))