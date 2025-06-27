from operator import index

from ds3.ds3_0_sorting import Sort, timer


class BucketSort(Sort):

    @timer
    def sort(self) -> None:
        self._sort(4)
        print()

    def _sort(self, count: int) -> None:
        buckets = [[] for _ in range(count)]
        for element in self.lst:
            buckets[element // count].append(element)
        for lst in buckets:
            lst.sort()
        idx = 0
        for bucket in buckets:
            for item in bucket:
                self.lst[idx] = item
                idx += 1



def main() -> None:
    obj = BucketSort()
    obj.sort()


if __name__ == '__main__':
    main()
