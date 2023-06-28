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

# Iterative solution


def dfs(root: Node, target: int):
    stack = [root]
    while len(stack) > 0:
        curr = stack.pop()  # leaves stack, node is 'visited'
        print(curr.val)
        if curr.val == target:
            return True
        if curr.right is not None:
            stack.append(curr.right)
        if curr.left is not None:
            stack.append(curr.left)
    return False

# Time: O(n)
# Space: O(n)


print(dfs(a, 4))


# recursive solution
def dfs_recrusive(root: Node, target: int):
    if root is None:
        return  # base case is trivially small

    print(root.val)
    dfs_recrusive(root.left, target)
    dfs_recrusive(root.right, target)


dfs_recrusive(a, 5)
