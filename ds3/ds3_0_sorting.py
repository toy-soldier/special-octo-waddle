import abc
import time
from typing import Callable


def timer(func: Callable[["Sort"], None]):
    def wrapper(self, *args, **kwargs):
        start = time.time()
        res = func(self, *args, **kwargs)
        duration = time.time() - start
        print(f"Method {self.__class__.__name__}.{func.__name__}() took {duration:.6f}s")
        return res
    return wrapper


class Sort(abc.ABC):
    def __init__(self):
        # self.lst = [i for i in range(1_000_000, 0, -1)]
        self.lst = [i for i in range(10, 0, -1)]

    @abc.abstractmethod
    def sort(self) -> None:
        pass

    def swap(self, index1: int, index2: int) -> None:
        if index1 == index2:
            return
        temp = self.lst[index1]
        self.lst[index1] = self.lst[index2]
        self.lst[index2] = temp
