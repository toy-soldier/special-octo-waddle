class HashTable:

    class _Entry:
        def __init__(self, key: int, value: str):
            self.key = key
            self.value = value

        def __str__(self):
            return f"{self.key}: {self.value}"

    def __init__(self, capacity: int):
        self._capacity = capacity
        self._table = [[] for _ in range(capacity)]

    def put(self, key: int, value: str) -> None:
        entries = self._get_entries(key)
        existing_entry = self._find_entry(key, entries)
        if existing_entry:
            existing_entry.value = value
        else:
            entries.append(self._Entry(key, value))

    def get(self, key: int) -> str|None:
        entries = self._get_entries(key)
        entry = self._find_entry(key, entries)
        return entry.value if entry else None

    def remove(self, key: int) -> None:
        entries = self._get_entries(key)
        entry = self._find_entry(key, entries)
        if entry:
            entries.remove(entry)

    def _get_entries(self, key: int) -> list[_Entry]:
        return self._table[key % self._capacity]

    @staticmethod
    def _find_entry(key: int, entries: list[_Entry]) -> _Entry | None:
        entry_list = [e for e in entries if e.key == key]
        return entry_list[0] if entry_list else None

    def __str__(self):
        return str(self._table)


def main():
    ht = HashTable(5)
    for i in range(65, 80):
        ht.put(i, chr(i))
    for i in range(65, 80):
        ht.put(i, chr(i))
    for i in range(65, 80):
        ht.put(i, chr(i).lower())
    ht.get(66)
    ht.get(73)
    ht.get(12)
    ht.remove(78)
    ht.remove(65)
    ht.remove(74)
    ht.remove(200)
    ht = HashTable(23)
    ht.remove(409)
    print()


if __name__ == "__main__":
    main()
