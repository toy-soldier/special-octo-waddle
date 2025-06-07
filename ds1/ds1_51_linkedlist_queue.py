import ds1_5_queue as queue
import ds1_3_linked_list as ll
import exceptions as exc


class LinkedListQueue(queue.Queue):

    def __init__(self):
        super().__init__()
        self._ll = ll.LinkedList()

    def enqueue(self, value: int) -> None:
        self._ll.add_last(value)
        self._count += 1

    def dequeue(self) -> int:
        value = self.peek()
        self._count -= 1
        self._ll.delete_first()
        return value

    def peek(self) -> int:
        if self.is_empty():
            raise exc.IsEmptyException("Queue is empty")
        return self._ll.get_kth_from_the_end(self._count)

    def __str__(self):
        return str(self._ll.to_array())


def main() -> None:
    q = LinkedListQueue()
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
