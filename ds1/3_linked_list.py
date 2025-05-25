class LinkedList:

    class _Node:

        def __init__(self, item: int):
            self.item = item
            self.next = None

        def __str__(self) -> str:
            return f"{self.item}->{self.next}"

    def __init__(self):
        self._first = None
        self._last = None
        self._size = 0

    def add_first(self, item: int) -> None:
        node = self._Node(item)
        if self.is_empty():
            self._last = node
        node.next = self._first
        self._first = node
        self._size += 1

    def add_last(self, item: int) -> None:
        node = self._Node(item)
        if self.is_empty():
            self._first = node
        else:
            self._last.next = node
        self._last = node
        self._size += 1

    def delete_first(self) -> None:
        if self.is_empty():
            return
        if self._first == self._last:  # only one list item so delete it immediately
            self._first = self._last = None
        else:
            self._first = self._first.next
        self._size -= 1

    def delete_last(self) -> None:
        if self.is_empty():
            return
        if self._first == self._last:  # only one list item so delete it immediately
            self._first = self._last = None
        else:
            rover = self._first
            while rover.next != self._last:
                rover = rover.next
            rover.next = None
            self ._last = rover
        self._size -= 1

    def contains(self, item: int) -> bool:
        return self.index_of(item) > -1

    def index_of(self, item: int) -> int:
        if self.is_empty():
            return -1

        index = 0
        rover = self._first
        while rover:
            index += 1
            if rover.item == item:
                return index
            rover = rover.next
        return -1

    def is_empty(self) -> bool:
        return self._first is None

    def size(self) -> int:
        return self._size

    def to_array(self) -> list[int]:
        lst = []
        if not self.is_empty():
            rover = self._first
            while rover:
                lst.append(rover.item)
                rover = rover.next
        return lst

    def reverse(self) -> None:
        one = None
        two = self._first
        while two:
            three = two.next
            two.next = one
            one = two
            two = three

        self._last = self._first
        self._first = one



def main() -> None:
    """Script entrypoint."""
    ll = LinkedList()
    print(ll.contains(10))
    print(ll.to_array())
    ll.add_last(40)
    ll.add_last(50)
    ll.add_last(60)
    ll.add_first(30)
    ll.add_first(20)
    ll.add_first(10)
    print(ll.contains(30))
    print(ll.contains(100))
    print(ll.to_array())
    ll.delete_last()
    ll.delete_first()
    ll.delete_last()
    ll.delete_last()
    ll.delete_first()
    print(ll.contains(30))
    print(ll.to_array())
    ll.delete_last()
    ll.delete_first()
    print(ll.to_array())
    ll.add_last(40)
    ll.add_last(50)
    ll.add_last(60)
    ll.add_first(30)
    ll.add_first(20)
    ll.add_first(10)
    print(ll.to_array())
    ll.reverse()
    print(ll.to_array())


if __name__ == "__main__":
    main()
