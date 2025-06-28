from ds31_0_searching import Search, timer


class BinarySearch(Search):

    @timer
    def search(self, value: int) -> int:
        self.lst.sort()
        return self._search(0, len(self.lst) - 1, value)

    def _search(self, start: int, end: int, value: int) -> int:
        if end < start:
            return -1

        middle = (start + end) // 2
        if self.lst[middle] > value:
            return self._search(start, middle - 1, value)
        if self.lst[middle] < value:
            return self._search(middle + 1, end, value)
        return middle


def main() -> None:
    obj = BinarySearch()
    print(obj.search(17))


if __name__ == '__main__':
    main()
