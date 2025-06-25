from ds3.ds3_0_sorting import Sort, timer


class SelectionSort(Sort):

    @timer
    def sort(self) -> None:
        for i in range(len(self.lst)):
            index_of_least = i
            for j in range(i, len(self.lst)):
                if self.lst[index_of_least] > self.lst[j]:
                    index_of_least = j
            self.swap(i, index_of_least)
        print()


def main() -> None:
    obj = SelectionSort()
    obj.sort()


if __name__ == '__main__':
    main()
