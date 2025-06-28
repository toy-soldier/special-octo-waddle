from ds31_0_searching import Search, timer


class TernarySearch(Search):

    @timer
    def search(self, value: int) -> int:
        self.lst.sort()
        return self._search(0, len(self.lst) - 1, value)

    def _search(self, start: int, end: int, value: int) -> int:
        if end < start:
            return -1

        part_size = (end - start) // 3
        boundary_1 = start + part_size
        boundary_2 = end - part_size

        if self.lst[boundary_1] > value:
            return self._search(start, boundary_1 - 1, value)
        if self.lst[boundary_1] == value:
            return boundary_1
        if self.lst[boundary_2] == value:
            return boundary_2
        if self.lst[boundary_2] < value:
            return self._search(boundary_2 + 1, end, value)
        return self._search(boundary_1 + 1, boundary_2 - 1, value)


def main() -> None:
    obj = TernarySearch()
    print(obj.search(26))


if __name__ == '__main__':
    main()
