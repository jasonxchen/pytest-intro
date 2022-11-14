# test adapted from https://codepen.io/GAmarketing/pen/jJOxBd?editors=0010

class BinaryNode:
    def __init__(self, data):
        # a node has data, left, and right pointers
        self.data = data
        # left and right are intialized as null
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        # when a new Tree is made, it has a root property
        self.root = None
    
    def insert(self, data):
        # add a new Node to the tree, with data as the Node's data
        new_node = BinaryNode(data)
        if not self.root:
            self.root = new_node
        else: 
            curr_node = self.root
            while curr_node:
                if new_node.data < curr_node.data:
                    if not curr_node.left:
                        curr_node.left = new_node
                        return
                    else:
                        curr_node = curr_node.left
                elif new_node.data > curr_node.data:
                    if not curr_node.right:
                        curr_node.right = new_node
                        return
                    else:
                        curr_node = curr_node.right
                else:
                    return
    
    def search(val):
        # search the Tree for a node with the given value
        # if the node exists, return it
        # if the node doesn't exist, return false
        pass
    
    def size(node):
        # calculate the number of nodes in the tree, starting from the given node
        pass
    
    def getMax():
        # return the maximum value stored in the tree
        pass
    
    def height(node):
        # calculate the maximum amount of nodes in any one path from the given node
        pass
    
    def isBalanced(node):
        # return true or false based on whether the sub-tree starting at the given node is balanced
        # A tree is imbalanced if the height of one branch exceeds the other side by more than one level
        # A tree is balanced if all branches end within one level of each other.
        pass
    

# Test Script below, DO NOT TOUCH 
import pytest

def test_node():
    new_node = BinaryNode(5)
    # should initialize with null left and right pointers
    assert new_node.left is None
    assert new_node.right is None
    
def test_tree1():
    tree = BinaryTree()
    # should initialize with a null root
    assert tree.root == None
    
def test_tree2():
    tree = BinaryTree()
    tree.insert(5)
    # should place the first node as the root
    assert tree.root.data == 5
    assert tree.root.left == None
    assert tree.root.right == None
    
def test_tree3():
    tree = BinaryTree()
    tree.insert(5)
    tree.insert(7)
    # should place new nodes according to Binary Tree rules
    assert tree.root.right.data == 7
    assert tree.root.left == None
    tree.insert(3)
    assert tree.root.left.data == 3
    tree.insert(1)
    assert tree.root.left.left.data == 1
    tree.insert(4)
    assert tree.root.left.right.data == 4
    tree.insert(9)
    assert tree.root.right.right.data == 9
    tree.insert(6)
    assert tree.root.right.left.data == 6
