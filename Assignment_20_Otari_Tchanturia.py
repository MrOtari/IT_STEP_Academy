class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return TreeNode(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        return node

    def printParent(self):
        print("Printing Parent Tree")
        self._printParent(self.root, None)

    def _printParent(self, node, parent):
        if node is not None:
            if parent is None:
                print(node.key, " -> Root")
            else:
                print(node.key, " -> ", parent.key)
            self._printParent(node.left, node)
            self._printParent(node.right, node)

    def printLeafNodes(self):
        print("Leaf Nodes:")
        self._printLeafNodes(self.root)

    def _printLeafNodes(self, node):
        if node is not None:
            if node.left is None and node.right is None:
                print(node.key)
            self._printLeafNodes(node.left)
            self._printLeafNodes(node.right)

    def countEdges(self):
        return self._countEdges(self.root)

    def _countEdges(self, node):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 0
        left_edges = self._countEdges(node.left)
        right_edges = self._countEdges(node.right)
        return left_edges + right_edges + 1

# Example usage:
binary_tree = BinaryTree()
binary_tree.insert(10)
binary_tree.insert(7)
binary_tree.insert(8)
binary_tree.insert(11)
binary_tree.insert(25)
binary_tree.insert(14)
binary_tree.insert(2)

binary_tree.printParent()

binary_tree.printLeafNodes()

print("Number of edges (internal nodes):", binary_tree.countEdges())