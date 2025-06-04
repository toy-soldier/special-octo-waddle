class Array:

    def __init__(self, length):
        self._lst = []

    def insert(self, item: int) -> None:
        self._lst.append(item)

    def remove_at(self, index: int) -> None:
        if len(self._lst) <= index:
            return
        self._lst.pop(index)

    def index_of(self, item: int) -> int:
        if item not in self._lst:
            return -1
        return self._lst.index(item)

    def max(self) -> int:
        if len(self._lst) == 0:
            return -1
        return max(self._lst)

    def intersect(self, other: list[int]) -> list[int]:
        common = []
        for i in self._lst:
            if i in other:
                common.append(i)
        return common

    def reverse(self):
        self._lst = self._lst[::-1]

    def insert_at(self, item: int, index: int) -> None:
        if len(self._lst) <= index:
            return
        self._lst.insert(index, item)

    def __str__(self):
        return str(self._lst)


def main() -> None:
    """Script entrypoint."""
    numbers = Array(3)
    print(numbers)
    numbers.insert(10)
    numbers.insert(20)
    numbers.insert(30)
    print(numbers)
    numbers.insert(40)
    numbers.remove_at(4)
    print(numbers)
    numbers.remove_at(3)
    print(numbers)
    print(numbers.index_of(20))
    print(numbers.index_of(1000))
    print(numbers.max())
    print(numbers.intersect([30,40,50]))
    numbers.reverse()
    print(numbers)
    numbers.insert_at(80, 5)
    print(numbers)



if __name__ == "__main__":
    main()
