class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
    a
  /   \ 
 b     c  
/ \     \
d  e     f
'''
a = Node(3)
b = Node(2)
c = Node(7)
d = Node(4)
e = Node(-2)
f = Node(5)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f


def bfs(root: Node, target: int):
    queue = [root]
    while len(queue) > 0:
        curr = queue.pop(0)
        if curr.val == target:
            return True
        if curr.left is not None:
            queue.append(curr.left)
        if curr.right is not None:
            queue.append(curr.right)

    return False


print(bfs(a, -2))
