from operator import index

from ds3.ds3_0_sorting import Sort, timer


class CountingSort(Sort):

    @timer
    def sort(self) -> None:
        self._sort(max(self.lst))
        print()

    def _sort(self, largest: int) -> None:
        counts = [0 for _ in range(largest + 1)]
        for element in self.lst:
            counts[element] += 1
        idx = 0
        for i, count in enumerate(counts):
            while count > 0:
                self.lst[idx] = i
                idx += 1
                count -= 1


def main() -> None:
    obj = CountingSort()
    obj.sort()


if __name__ == '__main__':
    main()
