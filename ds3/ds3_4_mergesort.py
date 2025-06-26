from ds3.ds3_0_sorting import Sort, timer


class MergeSort(Sort):

    @timer
    def sort(self) -> None:
        temp = self.lst.copy()
        self._split(0, len(self.lst) - 1, temp)
        print()

    def _split(self, start: int, end: int, temp: list[int]) -> None:
        if end - start == 0:  # List is of length 1 hence it's already sorted
            return
        mid = start + (end - start) // 2
        self._split(start, mid, temp)
        self._split(mid + 1, end, temp)
        self._merge(start, mid, mid + 1, end, temp)
        # now copy the merged partitions to the temp table
        for i in range(start, end + 1):
            temp[i] = self.lst[i]

    def _merge(self, s1: int, e1: int, s2: int, e2: int, temp: list[int]) -> None:
        index = s1
        while s1 <= e1 and s2 <= e2:
            if temp[s1] < temp[s2]:
                self.lst[index] = temp[s1]
                s1 += 1
            else:
                self.lst[index] = temp[s2]
                s2 += 1
            index += 1

        while s1 <= e1:      # in case partition 1 is not yet exhausted
            self.lst[index] = temp[s1]
            s1 += 1
            index += 1
        while s2 <= e2:      # in case partition 2 is not yet exhausted
            self.lst[index] = temp[s2]
            s2 += 1
            index += 1



def main() -> None:
    obj = MergeSort()
    obj.sort()


if __name__ == '__main__':
    main()
