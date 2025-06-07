import abc


class Queue(abc.ABC):

    def __init__(self):
        self._count = 0

    @abc.abstractmethod
    def enqueue(self, value: int) -> None:
        pass

    @abc.abstractmethod
    def dequeue(self) -> int:
        pass

    @abc.abstractmethod
    def peek(self) -> int:
        pass

    def get_count(self) -> int:
        return self._count

    def is_empty(self) -> bool:
        return self.get_count() == 0

    @abc.abstractmethod
    def __str__(self):
        pass
