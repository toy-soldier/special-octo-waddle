import ds1_5_queue as queue
import exceptions as exc


class CircularArrayQueue(queue.Queue):

    def __init__(self, capacity: int):
        super().__init__()
        self._front = self._rear = -1
        self._count = 0
        self._array = [0 for _ in range(capacity)]

    def enqueue(self, value: int) -> None:
        if self.is_full():
            raise exc.IsFullException("Queue is full")
        self._rear += 1
        if self._rear == len(self._array):
            self._rear = 0

        self._array[self._rear] = value
        self._count += 1
        if self._count == 1:
            self._front = self._rear

    def dequeue(self) -> int:
        value = self.peek()
        self._count -= 1
        self._front += 1
        if self._front == len(self._array):
            self._front = 0
        return value

    def peek(self) -> int:
        if self.is_empty():
            raise exc.IsEmptyException("Queue is empty")
        return self._array[self._front]

    def is_empty(self) -> bool:
        return self._count == 0

    def is_full(self) -> bool:
        return self._count == len(self._array)

    def __str__(self):
        if self.is_empty():
            return "[]"
        sz = len(self._array)
        if self._rear < self._front:
            back = self._rear + sz
        else:
            back = self._rear
        return str([self._array[i % sz] for i in range(self._front, back + 1)])


def main() -> None:
    q = CircularArrayQueue(3)
    print(q)
    q.enqueue(10)
    q.enqueue(20)
    q.dequeue()
    q.enqueue(40)
    q.enqueue(50)
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.enqueue(60)


if __name__ == "__main__":
    main()
