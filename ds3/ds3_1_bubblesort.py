from ds3.ds3_0_sorting import Sort, timer


class BubbleSort(Sort):

    @timer
    def sort(self) -> None:
        for i in range(len(self.lst) - 1, 0, -1):
            is_sorted = True
            for j in range(i):
                if self.lst[j] > self.lst[j+1]:
                    self.swap(j, j+1)
                    is_sorted = False
            if is_sorted:
                return
        print()


def main() -> None:
    obj = BubbleSort()
    obj.sort()


if __name__ == '__main__':
    main()
