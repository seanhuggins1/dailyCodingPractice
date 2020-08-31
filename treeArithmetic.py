import string

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



def evalTree(root):
    if root.data.isnumeric(): 
        return root.data
    result = str(
        eval(evalTree(root.left) + root.data + evalTree(root.right)))
    return result

print(evalTree(root))