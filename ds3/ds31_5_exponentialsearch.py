from ds31_0_searching import Search, timer
from ds31_2_binarysearch_recursive import BinarySearch


class ExponentialSearch(Search):

    @timer
    def search(self, value: int) -> int:
        self.lst.sort()
        size = len(self.lst)
        bound = 1
        while bound < size and self.lst[bound] < value:
            bound *= 2
        obj = BinarySearch()
        obj.lst.sort()
        return obj._search(bound // 2, min(bound, size - 1), value)



def main() -> None:
    obj = ExponentialSearch()
    print(obj.search(26))


if __name__ == '__main__':
    main()
