from ds31_0_searching import Search, timer


class JumpSearch(Search):

    @timer
    def search(self, value: int) -> int:
        self.lst.sort()
        block_size = int(pow(len(self.lst), 0.5))
        start = 0
        while True:
            end = min(start + block_size - 1, len(self.lst) - 1)
            if start > end:
                return -1
            if self.lst[end] == value:
                return end
            if self.lst[end] < value:
                start = end + 1
            else:
                for i in range(start, end + 1):
                    if self.lst[i] == value:
                        return i
                return -1


def main() -> None:
    obj = JumpSearch()
    print(obj.search(26))


if __name__ == '__main__':
    main()
