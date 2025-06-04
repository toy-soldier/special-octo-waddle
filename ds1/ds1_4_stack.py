import ds1_3_linked_list as ll
import exceptions as exc


class Stack:

    def __init__(self):
        self._ll = ll.LinkedList()

    def push(self, item: int) -> None:
        self._ll.add_last(item)

    def peek(self) -> int:
        if self.is_empty():
            raise exc.IsEmptyException("Stack is empty")
        return self._ll.get_kth_from_the_end(1)

    def pop(self) -> int:
        top = self.peek()
        self._ll.delete_last()
        return top

    def is_empty(self) -> bool:
        return self._ll.is_empty()

    def __str__(self):
        return str(self._ll.to_array())


def main() -> None:
    """Script entrypoint."""
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print(stack)
    print(stack.pop())
    print(stack)
    print(stack.peek())
    print(stack)
    print(stack.is_empty())
    stack.pop()
    stack.pop()
    print(stack)
    print(stack.is_empty())



if __name__ == "__main__":
    main()
