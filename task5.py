from collections import deque

def s():
    ans = []

    class Node:
        def __init__(self, val):
            self.val = val
            self.left = None
            self.right = None

    def print_tree(node):
        queue = deque()
        visited = set()

        queue.append(node)
        while queue:

            now = queue.popleft()
            visited.add(now.val)
            ans.append(now.val)

            if now.right and now.right.val not in visited:
            #Если правый сын существует и его нет в посещенных
                queue.append(now.right)
            if now.left and now.left.val not in visited:
                queue.append(now.left)


    root = Node(8)
    root.right = Node(5)
    root.left = Node(10)

    root.left.right = Node(3)
    root.left.left = Node(6)

    root.right.right = Node(11)
    root.right.left = Node(9)

    print_tree(root)
    return (ans)
    # :-)
if __name__ == '__main__':
    print(*s())
    # 8 5 10 11 9 3 6