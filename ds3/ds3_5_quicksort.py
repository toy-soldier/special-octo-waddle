from operator import index

from ds3.ds3_0_sorting import Sort, timer


class QuickSort(Sort):

    @timer
    def sort(self) -> None:
        self._partition(0, len(self.lst) - 1)
        print()

    def _partition(self, start: int, end: int) -> None:
        if end - start < 1:  # List is of length 1 or 0, hence it's already sorted
            return
        boundary = start - 1
        pivot = end
        for i in range(start, pivot + 1):
            if self.lst[i] < self.lst[pivot]:
                boundary += 1
                self.swap(boundary, i)
        boundary += 1
        self.swap(boundary, pivot)
        self._partition(start, boundary - 1)
        self._partition(boundary + 1, end)



def main() -> None:
    obj = QuickSort()
    obj.sort()


if __name__ == '__main__':
    main()
