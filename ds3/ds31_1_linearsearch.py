from ds31_0_searching import Search, timer


class LinearSearch(Search):

    @timer
    def search(self, value: int) -> int:
        for i, item in enumerate(self.lst):
            if value == item:
                return i
        return -1


def main() -> None:
    obj = LinearSearch()
    print(obj.search(17))


if __name__ == '__main__':
    main()
