class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def printPreorder(root):
    if root:
        print(root.val),
        printPreorder(root.left)
        printPreorder(root.right)

def printPostorder(root):
    if root:
        printPostorder(root.left)
        printPostorder(root.right)
        print(root.val)

def printInorder(root): 
    if root:
        printInorder(root.left)
        print(root.val)
        printInorder(root.right)
 
root = Node(30)
root.left = Node(20)
root.right = Node(40)
root.left.left = Node(15)
root.left.right = Node(25)
print("Preorder traversal of binary tree is")
printPreorder(root)

print ("\nPostorder traversal of binary tree is")
printPostorder(root)

print("\n Inorder traversal of binary tree is")
printInorder(root)