import ds1_5_queue as queue
import ds1_4_stack as s
import exceptions as exc


class TwoStacksQueue(queue.Queue):

    def __init__(self):
        super().__init__()
        self._stack1 = s.Stack()
        self._stack2 = s.Stack()

    def enqueue(self, value: int) -> None:
        self._stack1.push(value)
        self._count += 1

    def dequeue(self) -> int:
        value = self.peek()
        self._count -= 1
        self._stack2.pop()
        return value

    def peek(self) -> int:
        if self.is_empty():
            raise exc.IsEmptyException("Queue is empty")
        if self._stack2.is_empty():
            while not self._stack1.is_empty():
                self._stack2.push(self._stack1.pop())
        return self._stack2.peek()

    def __str__(self):
        return f"s1->{self._stack1}, s2->{self._stack2}"


def main() -> None:
    q = TwoStacksQueue()
    q.enqueue(10)
    q.enqueue(20)
    q.dequeue()
    q.enqueue(40)
    q.enqueue(50)
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.enqueue(60)
    print()


if __name__ == "__main__":
    main()
