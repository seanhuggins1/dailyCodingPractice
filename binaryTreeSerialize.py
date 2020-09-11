class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right




def serialize(root):
    result = ''
    if root: 
        result = root.val + ','
        result += serialize(root.left)
        result += serialize(root.right)
    return result

def deserialize(s):
    s = s.split(',')
    for i in range(len(s)):
        s[i] = s[i].split('.')

    root = Node(s[0])
    for i in range(1, len(s) - 1):
        current = root
        for k in s[i]:
            if (k == 'left'): 
                current.left = Node(s[i])
                current = current.left
            if (k == 'right'):
                current.right = Node(s[i])
                current = current.right





node = Node('root', Node('left', Node('left.left'), Node('left.right')), Node('right', Node('right.left'), Node('right.right')))


deserialize(serialize(node))


assert deserialize(serialize(node)).left.left.val == 'left.left'        