import abc
import time
from typing import Callable


def timer(func: Callable[["Search"], None]):
    def wrapper(self, *args, **kwargs):
        start = time.time()
        res = func(self, *args, **kwargs)
        duration = time.time() - start
        print(f"Method {self.__class__.__name__}.{func.__name__}() took {duration:.6f}s")
        return res
    return wrapper


class Search(abc.ABC):
    def __init__(self):
        # self.lst = [i for i in range(1_000_000, 0, -1)]
        self.lst = [i for i in range(25, 0, -1)]

    @abc.abstractmethod
    def search(self, value: int) -> int:
        pass
