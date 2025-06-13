from typing import Self
import exceptions as exc


class Tree:
    class _Node:
        def __init__(self, value: int):
            self.value = value
            self.left_child = self.right_child = None

        def __str__(self):
            return f"Node={self.value}"

    def __init__(self):
        self._root = None

    def insert(self, value: int) -> None:
        node = self._Node(value)
        if not self._root:
            self._root = node
            return
        last, remark = self._find_last_node(value)
        if remark == "left":
            last.left_child = node
        elif remark == "right":
            last.right_child = node

    def find(self, value: int) -> bool:
        return self._find_last_node(value)[1] == "found"

    def _find_last_node(self, value: int) -> tuple[_Node, str]:
        last = current = self._root
        remark = ""

        while current:
            last = current
            if value < current.value:
                current = current.left_child
                remark = "left"
            elif value > current.value:
                current = current.right_child
                remark = "right"
            else:
                current = None
                remark = "found"
        return last, remark

    def level_order_traversal(self) -> list[int]:
        node_queue = [self._root]
        list_of_nodes = []
        while node_queue:
            node = node_queue.pop(0)
            list_of_nodes.append(node.value)
            left = node.left_child
            right = node.right_child
            if left:
                node_queue.append(left)
            if right:
                node_queue.append(right)
        return list_of_nodes

    def pre_order_traversal(self) -> list[int]:
        return self._pre_order(self._root, [])

    def _pre_order(self, root: _Node, nodes: list[int]) -> list[int]:
        if not root:
            return nodes
        nodes.append(root.value)
        self._pre_order(root.left_child, nodes)
        self._pre_order(root.right_child, nodes)
        return nodes

    def in_order_traversal(self) -> list[int]:
        return self._in_order(self._root, [])

    def _in_order(self, root: _Node, nodes: list[int]) -> list[int]:
        if not root:
            return nodes
        self._in_order(root.left_child, nodes)
        nodes.append(root.value)
        self._in_order(root.right_child, nodes)
        return nodes

    def post_order_traversal(self) -> list[int]:
        return self._post_order(self._root, [])

    def _post_order(self, root: _Node, nodes: list[int]) -> list[int]:
        if not root:
            return nodes
        self._post_order(root.left_child, nodes)
        self._post_order(root.right_child, nodes)
        nodes.append(root.value)
        return nodes

    def height(self) -> int:
        if not self._root:
            raise exc.IsEmptyException("Tree is empty")
        return self._height(self._root)

    def _height(self, root: _Node) -> int:
        if not root:
            return -1
        if self._is_leaf(root):
            return 0
        return 1 + max(self._height(root.left_child), self._height(root.right_child))

    @staticmethod
    def _is_leaf(root: _Node) -> bool:
        return not root.left_child and not root.right_child

    def min(self) -> int:
        if not self._root:
            raise exc.IsEmptyException("Tree is empty")
        return self._min(self._root)

    def _min(self, root: _Node) -> int:
        if not root:
            return -1
        if self._is_leaf(root):
            return root.value
        return min(root.value, self._min(root.left_child), self._min(root.right_child))

    def max(self) -> int:
        if not self._root:
            raise exc.IsEmptyException("Tree is empty")
        return self._max(self._root)

    def _max(self, root: _Node) -> int:
        if not root:
            return -1
        if self._is_leaf(root):
            return root.value
        return max(root.value, self._max(root.left_child), self._max(root.right_child))

    def size(self) -> int:
        if not self._root:
            raise exc.IsEmptyException("Tree is empty")
        return self._size(self._root)

    def _size(self, root: _Node) -> int:
        if not root:
            return 0
        if self._is_leaf(root):
            return 1
        return 1 + self._size(root.left_child) + self._size(root.right_child)

    def count_leaves(self) -> int:
        if not self._root:
            raise exc.IsEmptyException("Tree is empty")
        return self._count_leaves(self._root)

    def _count_leaves(self, root: _Node) -> int:
        if not root:
            return 0
        if self._is_leaf(root):
            return 1
        return self._count_leaves(root.left_child) + self._count_leaves(root.right_child)

    def contains(self, value: int) -> bool:
        if not self._root:
            raise exc.IsEmptyException("Tree is empty")
        return self._contains(self._root, value)

    def _contains(self, root: _Node, value: int) -> bool:
        if not root:
            return False
        if root.value == value:
            return True
        return (self._contains(root.left_child, value)
                or self._contains(root.right_child, value))

    def equals(self, other: Self) -> bool:
        if not self._root or not other._root:
            raise exc.IsEmptyException("Tree is empty")
        return self._equals(self._root, other._root)

    def _equals(self, root: _Node, other: _Node) -> bool:
        if not root and not other:
            return True
        if root and other:
            return (root.value == other.value
                and self._equals(root.left_child, other.left_child)
                and self._equals(root.right_child, other.right_child))
        return False

    def are_siblings(self, value1: int, value2: int) -> bool:
        if not self._root:
            raise exc.IsEmptyException("Tree is empty")
        node1 = self._find_parent(self._root, value1)
        node2 = self._find_parent(self._root, value2)
        return node1 is not None and node2 is not None and node1 == node2

    def _find_parent(self, root: _Node, value: int) -> _Node | None:
        if not root:
            return None
        if self._is_leaf(root):
            return None

        left = root.left_child
        right = root.right_child
        if left.value == value or right.value == value:
            return root

        return (self._find_parent(left, value)
                or self._find_parent(right, value))

    def create_invalid_tree(self) -> None:
        self.insert(10)
        self.insert(6)
        self.insert(21)
        self.insert(3)
        self.insert(8)
        r = self._root
        self._root = self._Node(20)
        self._root.left_child = r
        self._root.right_child = self._Node(30)
        self._root.right_child.left_child = self._Node(4)

    def is_bst(self) -> bool:
        if not self._root:
            raise exc.IsEmptyException("Tree is empty")
        return self._is_bst(self._root, -999_999, 999_999)

    def _is_bst(self, root: _Node, min_value: int, max_value: int) -> bool:
        if not root:
            return True
        if min_value < root.value < max_value:
            return (self._is_bst(root.left_child, min_value=min_value, max_value=root.value)
                    and self._is_bst(root.right_child, min_value=root.value, max_value=max_value))
        return False

    def nodes_at_k_distance(self, k: int) -> list[_Node]:
        if not self._root:
            raise exc.IsEmptyException("Tree is empty")
        return self._nodes_at_k_distance(self._root, k, [])

    def _nodes_at_k_distance(self, root: _Node, k: int, nodes: list[_Node]) -> list[_Node] | None:
        if not root:
            return
        if k == 0:
            nodes.append(root)
        else:
            self._nodes_at_k_distance(root.left_child, k - 1, nodes)
            self._nodes_at_k_distance(root.right_child, k - 1, nodes)
        return nodes

    def get_ancestors(self, value: int) -> list[_Node]:
        if not self._root:
            raise exc.IsEmptyException("Tree is empty")
        ancestors = []
        self._get_ancestors(self._root, value, ancestors)
        return ancestors

    def _get_ancestors(self, root: _Node, value: int, ancestors: list[_Node]) -> bool:
        if not root:
            return False
        if root.value == value:
            return True
        if (self._get_ancestors(root.left_child, value, ancestors)
            or self._get_ancestors(root.right_child, value, ancestors)):
            ancestors.append(root)
            return True  # to ensure that the parent of this ancestor is also added to the list
        return False

    def __str__(self):
        return f"{self._root}"


def main():
    t = Tree()
    t.insert(7)
    t.insert(4)
    t.insert(9)
    t.insert(1)
    t.insert(6)
    t.insert(8)
    t.insert(10)
    a=t.find(7)
    a=t.find(4)
    a=t.find(20)
    a=t.find(10)
    a=t.level_order_traversal()
    a=t.pre_order_traversal()
    a=t.in_order_traversal()
    a=t.post_order_traversal()
    a=t.height()
    a=t.min()
    a=t.max()
    a=t.size()
    a=t.count_leaves()
    a=t.contains(7)
    a=t.contains(4)
    a=t.contains(20)
    a=t.contains(10)
    a=t.are_siblings(8,1)
    s = Tree()
    s.insert(7)
    s.insert(4)
    s.insert(9)
    s.insert(1)
    s.insert(6)
    s.insert(8)
    s.insert(10)
    a=s.equals(t)
    i = Tree()
    i.create_invalid_tree()
    a=i.is_bst()
    a=i.nodes_at_k_distance(3)
    a=t.get_ancestors(10)
    print()


if __name__ == '__main__':
    main()
