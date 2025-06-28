from ds31_0_searching import Search, timer


class BinarySearch(Search):

    @timer
    def search(self, value: int) -> int:
        self.lst.sort()
        start = 0
        end = len(self.lst) - 1
        while start <= end:
            middle = (start + end) // 2
            if self.lst[middle] > value:
                end = middle - 1
            elif self.lst[middle] < value:
                start = middle + 1
            else:
                return middle
        return -1



def main() -> None:
    obj = BinarySearch()
    print(obj.search(17))


if __name__ == '__main__':
    main()
