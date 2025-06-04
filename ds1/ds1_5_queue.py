import abc


class Queue(abc.ABC):

    def __init__(self):
        self._front = None
        self._rear = None

    @abc.abstractmethod
    def enqueue(self, value: int) -> None:
        pass

    @abc.abstractmethod
    def dequeue(self) -> int:
        pass

    @abc.abstractmethod
    def peek(self) -> int:
        pass

    @abc.abstractmethod
    def is_empty(self) -> bool:
        pass

    @abc.abstractmethod
    def is_full(self) -> bool:
        pass

    @abc.abstractmethod
    def __str__(self):
        pass
