import exceptions


def heapify(numbers: list[int]) -> list[int]:
    # optimizations:
    # 1. no need to iterate over the leaf nodes because surely they have no children
    # 2. start from the last parent so these nodes are already in their proper place;
    #   as we go up the tree, we may not need to perform heapify() on these nodes
    index_of_last_parent = len(numbers) // 2 - 1
    for i in range(index_of_last_parent, -1, -1):
        move_to_proper_place(numbers, i)
    return numbers


def move_to_proper_place(numbers: list[int], index: int) -> None:
    index_of_largest = get_index_of_largest_node(numbers, index)
    if index_of_largest == index:  # node is in proper place, nothing to do
        return
    swap(numbers, index, index_of_largest)
    move_to_proper_place(numbers, index_of_largest)


def get_index_of_largest_node(numbers: list[int], index: int) -> int:
    index_of_largest = index
    index_of_left = 2 * index + 1
    index_of_right = index_of_left + 1
    if index_of_left < len(numbers) and numbers[index_of_left] > numbers[index_of_largest]:
        index_of_largest = index_of_left
    if index_of_right < len(numbers) and numbers[index_of_right] > numbers[index_of_largest]:
        index_of_largest = index_of_right
    return index_of_largest


def swap(numbers: list[int], first: int, second: int) -> None:
    temp = numbers[first]
    numbers[first] = numbers[second]
    numbers[second] = temp


def is_max_heap(numbers: list[int]) -> bool:
    index_of_last_parent = len(numbers) // 2 - 1
    for i in range(index_of_last_parent, -1, -1):
        if get_index_of_largest_node(numbers, i) != i:
            return False
    return True


class Heap:
    def __init__(self):
        self._items = []
        self._size = 0

    def insert(self, value: int) -> None:
        self._items.append(value)
        self._size += 1
        self._bubble_up()

    def remove(self) -> int:
        if self.is_empty():
            raise exceptions.IsEmptyException("Heap is empty")
        self._size -= 1
        self._swap(0, self._size)
        value = self._items.pop()
        self._bubble_down()
        return value

    def is_empty(self):
        return self._size == 0

    def kth_largest_item(self, k: int) -> int:
        if self.is_empty():
            raise exceptions.IsEmptyException("Heap is empty")
        if not 0 < k < self._size:
            raise exceptions.IllegalArgumentException("k is invalid")
        value = None
        for _ in range(k):
            value = self.remove()
        return value

    def _bubble_up(self) -> None:
        index = self._size - 1
        while (index > 0
            and self._items[self._get_parent_index(index)] < self._items[index]):
            self._swap(self._get_parent_index(index), index)
            index = self._get_parent_index(index)

    def _bubble_down(self) -> None:
        index = 0
        while ((child := self._get_child_index(index)) < self._size
               and self._items[child] > self._items[index]):
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
        if self._items[child1] > self._items[child2]:  # both children exist so compare
            return child1
        return child2

    def _swap(self, first: int, second: int) -> None:
        temp = self._items[first]
        self._items[first] = self._items[second]
        self._items[second] = temp

    def __str__(self):
        return str(self._items)


def main() -> None:
    h = Heap()
    for i in (15, 10, 3, 8, 12, 9, 4, 1, 24):
        h.insert(i)
    a = h.remove()
    a = heapify([8, 15, 9, 12, 10, 3, 4, 1])
    a = h.kth_largest_item(4)
    a = is_max_heap([8, 15, 9, 12, 10, 3, 4, 1])
    a = is_max_heap(heapify([8, 15, 9, 12, 10, 3, 4, 1]))
    print()


if __name__ == "__main__":
    main()
