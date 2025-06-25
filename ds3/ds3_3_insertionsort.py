from ds3.ds3_0_sorting import Sort, timer


class InsertionSort(Sort):

    @timer
    def sort(self) -> None:
        for i in range(1, len(self.lst)):
            current = self.lst[i]
            j = i - 1
            while j >= 0 and self.lst[j] > current:
                self.lst[j+1] = self.lst[j]
                j -= 1
            self.lst[j+1] = current
        print()


def main() -> None:
    obj = InsertionSort()
    obj.sort()


if __name__ == '__main__':
    main()
