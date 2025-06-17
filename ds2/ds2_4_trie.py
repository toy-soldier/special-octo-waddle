from typing import Self
import exceptions


class Trie:

    class _Node:
        def __init__(self, value: str):
            self.value = value
            self.children = {}
            self.is_end_of_word = False

        def has_children(self) -> bool:
            return self.children != {}

        def get_children(self) -> list[Self]:
            return list(self.children.values())

        def get_child(self, value: str) -> Self | None:
            return self.children.get(value)

        def add_child(self, value: str) -> None:
            self.children[value] = self.__class__(value)

        def delete_child(self, value: str) -> None:
            self.children.pop(value)

        @property
        def is_end_of_word(self) -> bool:
            return self._is_end_of_word

        @is_end_of_word.setter
        def is_end_of_word(self, flag: bool) -> None:
            self._is_end_of_word = flag

        def __str__(self):
            return f"{self.value}{'*' if self.is_end_of_word else ''}"

    def __init__(self):
        self._root = self._Node("")

    def get_root(self) -> _Node:
        return self._root

    def insert(self, word: str) -> None:
        if not word or word.strip() == "":
            return
        current = self._root
        for letter in word.lower():
            child = current.get_child(letter)
            if not child:
                current.add_child(letter)
                child = current.get_child(letter)
            current = child
        current.is_end_of_word = True

    def contains(self, word: str) -> bool:
        current = self._find_last_node(word)
        return current is not None and current.is_end_of_word

    def remove(self, word: str) -> None:
        if not word:
            return
        self._remove(self._root, word, 0)

    def _remove(self, root: _Node, word: str, index: int) -> None:
        if index == len(word):
            root.is_end_of_word = False
            return

        letter = word[index]
        child = root.get_child(letter)
        if not child:
            return

        self._remove(child, word, index + 1)

        if not child.has_children() and not child.is_end_of_word:
            root.delete_child(letter)

    def autocomplete(self, word: str) -> list[str]:
        suggestions = []
        current = self._find_last_node(word)
        if not word or not current:
            return suggestions

        self._autocomplete(current, word, suggestions)
        return suggestions

    def _autocomplete(self, root: _Node, word: str, suggestions: list[str]) -> None:
        if root.is_end_of_word:
            suggestions.append(word)
        for child in root.get_children():
            self._autocomplete(child, word + child.value, suggestions)

    def _find_last_node(self, word: str) -> _Node | None:
        if not word:
            return None
        current = self._root
        for letter in word.lower():
            current = current.get_child(letter)
            if not current:
                return None
        return current

    def contains_recursive(self, word: str) -> bool:
        if not word:
            return False

        return self._has(self._root, word, 0)

    def _has(self, root: _Node, word: str, index: int) -> bool:
        if index == len(word):
            return root.is_end_of_word

        letter = word[index]
        root = root.get_child(letter)
        if not root:
            return False
        return self._has(root, word, index + 1)

    def count_words(self) -> int:
        return self._count_words(self._root)

    def _count_words(self, root: _Node) -> int:
        count = 0

        if not root:
            return 0
        if root.is_end_of_word:
            count += 1
        for child in root.get_children():
            count += self._count_words(child)

        return count


def longest_common_prefix(words: list[str]) -> str:
    prefix = []
    t = Trie()
    for word in words:
        t.insert(word)

    current = t.get_root()
    while current:
        prefix.append(current.value)
        children = current.get_children()
        if len(children) != 1 or current.is_end_of_word:
            break
        current = children[0]
    return "".join(prefix)


def main() -> None:
    t = Trie()
    t.insert("boy")
    t.insert("boyfriend")
    t.insert("bookworm")
    t.insert("girl")
    print(t.count_words())
    a = t.contains("boy")
    a = t.contains("apple")
    a = t.contains("boycott")
    a = t.contains("book")
    a = t.contains("boyfriend")
    a = t.contains("bookworm")
    t.remove("girl")
    t.remove("book")
    t.remove("boyfriend")
    a = t.contains("boy")
    a = t.contains("girl")
    a = t.contains("boyfriend")
    a = t.contains("bookworm")
    print(t.count_words())
    print()
    t = Trie()
    t.insert("car")
    t.insert("care")
    t.insert("card")
    t.insert("careful")
    t.insert("egg")
    a = t.autocomplete("c")
    print(a)
    print(t.contains(None))
    print(t.contains_recursive(None))
    print(t.count_words())
    print(longest_common_prefix(["can", "canada", "care", "cab"]))


if __name__ == '__main__':
    main()
