import exceptions


class Heap:

    class _Node:
        def __init__(self, key: int, value: str):
            self.key = key
            self.value = value

        def __str__(self):
            return f"Node {self.key}:{self.value}"

    def __init__(self):
        self._items = []
        self._size = 0

    def insert(self, key: int, value: str) -> None:
        node = self._Node(key, value)
        self._items.append(node)
        self._size += 1
        self._bubble_up()

    def remove(self) -> int:
        if self.is_empty():
            raise exceptions.IsEmptyException("Heap is empty")
        self._size -= 1
        self._swap(0, self._size)
        node = self._items.pop()
        self._bubble_down()
        return node

    def is_empty(self):
        return self._size == 0

    def _bubble_up(self) -> None:
        index = self._size - 1
        while (index > 0
            and self._items[self._get_parent_index(index)].key > self._items[index].key):
            self._swap(self._get_parent_index(index), index)
            index = self._get_parent_index(index)

    def _bubble_down(self) -> None:
        index = 0
        while ((child := self._get_child_index(index)) < self._size
               and self._items[child].key < self._items[index].key):
            self._swap(child, index)
            index = child

    @staticmethod
    def _get_parent_index(index: int) -> int:
        return (index - 1) // 2

    def _get_child_index(self, index: int) -> int:
        child1 = index * 2 + 1
        child2 = child1 + 1

        if child1 >= self._size:  # items[index] has no children so return some invalid index
            return self._size
        if child2 >= self._size:  # items[index] only has a left child so return its index
            return child1
        if self._items[child1].key < self._items[child2].key:  # both children exist so compare
            return child1
        return child2

    def _swap(self, first: int, second: int) -> None:
        temp = self._items[first]
        self._items[first] = self._items[second]
        self._items[second] = temp

    def __str__(self):
        return str([str(node) for node in self._items])


def main() -> None:
    h = Heap()
    for i in (15, 10, 3, 8, 12, 9, 4, 1, 24):
        h.insert(i, chr(64 + i))
    a = h.remove()
    a = h.remove()
    print()


if __name__ == "__main__":
    main()
