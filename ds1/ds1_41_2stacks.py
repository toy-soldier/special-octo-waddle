import exceptions as exc


VERY_SMALL_NUMBER = -99999999

class TwoStacks:

    def __init__(self, capacity: int):
        self._array = [VERY_SMALL_NUMBER for _ in range(capacity)]
        self._top1 = -1
        self._top2 = capacity

    def is_full1(self) -> bool:
        return self._top1 + 1 == self._top2

    def is_full2(self) -> bool:
        return self._top2 - 1 == self._top1

    def is_empty1(self) -> bool:
        return self._top1 == -1

    def is_empty2(self) -> bool:
        return self._top2 == len(self._array)

    def push1(self, item: int) -> None:
        if self.is_full1():
            raise Exception("Stack is full")
        self._top1 += 1
        self._array[self._top1] = item

    def push2(self, item: int) -> None:
        if self.is_full2():
            raise Exception("Stack is full")
        self._top2 -= 1
        self._array[self._top2] = item

    def peek1(self) -> int:
        if self.is_empty1():
            raise exc.IsEmptyException("Stack is empty")
        return self._array[self._top1]

    def peek2(self) -> int:
        if self.is_empty2():
            raise exc.IsEmptyException("Stack is empty")
        return self._array[self._top2]

    def pop1(self) -> int:
        top = self.peek1()
        self._array[self._top1] = VERY_SMALL_NUMBER
        self._top1 -= 1
        return top

    def pop2(self) -> int:
        top = self.peek2()
        self._array[self._top2] = VERY_SMALL_NUMBER
        self._top2 += 1
        return top

    def __str__(self):
        return str(self._array)


def main() -> None:
    """Script entrypoint."""
    stack = TwoStacks(4)
    stack.push1(10)
    stack.push1(20)
    stack.push2(130)
    print(stack)
    print(stack.pop1())
    print(stack)
    print(stack.peek2())
    print(stack)
    print(stack.is_empty1())
    stack.pop1()
    stack.pop2()
    print(stack)
    print(stack.is_empty1())



if __name__ == "__main__":
    main()
