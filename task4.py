
def s():
    ans = []

    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

    def print_tree(node):
        if node is not None:
            print_tree(node.left)
            ans.append(node.data)
            print_tree(node.right)


    root = Node(8)
    root.right = Node(5)
    root.left = Node(10)

    root.left.right = Node(3)
    root.left.left = Node(6)

    root.right.right = Node(11)
    root.right.left = Node(9)

    print_tree(root)
    return (sorted(ans))
    # :-)
if __name__ == '__main__':
    print(s())