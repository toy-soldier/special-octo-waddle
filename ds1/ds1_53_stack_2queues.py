import ds1_51_linkedlist_queue as ll
import exceptions as exc


class Stack:

    def __init__(self):
        self._queue_for_insert = ll.LinkedListQueue()
        self._spare_queue = ll.LinkedListQueue()

    def push(self, item: int) -> None:
        self._queue_for_insert.enqueue(item)

    def peek(self) -> int:
        if self._queue_for_insert.is_empty():
            raise exc.IsEmptyException("Stack is empty")
        while self._queue_for_insert.get_count() > 1:
            self._spare_queue.enqueue(self._queue_for_insert.dequeue())
        return self._queue_for_insert.peek()

    def pop(self) -> int:
        top = self.peek()
        self._queue_for_insert.dequeue()
        self._swap_queues()
        return top

    def is_empty(self) -> bool:
        return self._queue_for_insert.is_empty()

    def _swap_queues(self) -> None:
        temp = self._queue_for_insert
        self._queue_for_insert = self._spare_queue
        self._spare_queue = temp

    def __str__(self):
        return f"for_inserts->{self._queue_for_insert}, spare->{self._spare_queue}"


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
