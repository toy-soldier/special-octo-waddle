class AVLTree:

    class _Node:
        def __init__(self, value: int):
            self.value = value
            self.left_child = self.right_child = None
            self.height = 0
            self.balance_factor = 0

        def __str__(self):
            return f"Node={self.value}"

    def insert(self, value: int) -> None:
        self._root = self._insert(self._root, value)

    def _insert(self, root: _Node, value: int) -> _Node:
        if not root:
            return self._Node(value)
        if value < root.value:
            root.left_child = self._insert(root.left_child, value)
        else:
            root.right_child = self._insert(root.right_child, value)

        self._compute_stats(root)
        root = self._balance(root)
        return root

    def _balance(self, root: _Node) -> _Node:
        if root.balance_factor < -1:  # root is right heavy
            if root.right_child.balance_factor > 0:  # right child is left heavy
                root.right_child = self._right_rotate(root.right_child)
            root = self._left_rotate(root)

        if root.balance_factor > 1:  # root is left heavy
            if root.left_child.balance_factor < 0:  # left child is right heavy
                root.left_child = self._left_rotate(root.left_child)
            root = self._right_rotate(root)

        return root

    def _compute_stats(self, root: _Node) -> None:
        left_height = self._height(root.left_child)
        right_height = self._height(root.right_child)
        root.height = 1 + max(left_height, right_height)
        root.balance_factor = left_height - right_height

    @staticmethod
    def _height(node: _Node) -> int:
        return node.height if node else -1

    def _left_rotate(self, root: _Node) -> _Node:
        new_root = root.right_child
        root.right_child = new_root.left_child
        new_root.left_child = root

        self._compute_stats(root)
        self._compute_stats(new_root)
        return new_root

    def _right_rotate(self, root: _Node) -> _Node:
        new_root = root.left_child
        root.left_child = new_root.right_child
        new_root.right_child = root

        self._compute_stats(root)
        self._compute_stats(new_root)
        return new_root

    def is_balanced(self) -> bool:
        return self._root.balance_factor in {-1, 0, 1}

    def is_perfect(self) -> bool:
        height = self._root.height
        return pow(2, height) <= self._size(self._root) < pow(2, height + 1)

    def _size(self, root: _Node) -> int:
        if not root:
            return 0
        return 1 + self._size(root.left_child) + self._size(root.right_child)

    def __init__(self):
        self._root = None


def main() -> None:
    t = AVLTree()
    t.insert(30)
    t.insert(15)
    t.insert(18)
    t.insert(10)
    t.insert(16)
    t.insert(7)
    t.insert(8)
    a=t.is_balanced()
    a=t.is_perfect()
    print()


if __name__ == '__main__':
    main()
