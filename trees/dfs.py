class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
    a(3)
  /      \ 
 b(2)     c(7)  
/     \       \
d(4)  e(-2)     f(5)
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

# Recurisve


def dfs(root: Node, target: int):
    stack = [root]
    while len(stack) > 0:
        curr = stack.pop()
        print(curr.val)
        if curr.val == target:
            return True
        if curr.left is not None:
            stack.append(curr.left)
        if curr.right is not None:
            stack.append(curr.right)
    return False


print(dfs(a, -2))
