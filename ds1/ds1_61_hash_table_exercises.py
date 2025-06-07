def most_frequent(numbers: list[int]) -> int|None:
    frequencies = {}
    most = None
    count = 0
    for i in numbers:
        frequencies[i] = frequencies.get(i, 0) + 1
    for k, v in frequencies.items():
        if v > count:
            count = v
            most = k

    return most


def get_pairs(length: int) -> list[tuple[int, int]]:
    pairs = []
    for i in range(length - 1):
        for j in range(i + 1, length):
            pairs.append((i, j))
    return pairs


def count_pairs_with_diff_slow(numbers: list[int], k: int) -> int:
    # O(n^2)
    count = 0
    pairs = get_pairs(len(numbers))
    for i, j in pairs:
        if abs(numbers[i] - numbers[j]) == k:
            count += 1
    return count


def count_pairs_with_diff(numbers: list[int], k: int) -> int:
    # O(n)
    numbers_set = set(numbers)
    count = 0
    for n in numbers:
        if n + k in numbers_set:
            count += 1
        if n - k in numbers_set:
            count += 1
        # the pair (n, x) is also (x, n); when we later encounter x we won't pair it with n, to prevents double counting
        numbers_set.remove(n)
    return count


def two_sum_slow(numbers: list[int], target: int) -> list[int]|None:
    # O(n^2)
    pairs = get_pairs(len(numbers))
    for i, j in pairs:
        if numbers[i] + numbers[j] == target:
            return [i, j]
    return None


def two_sum(numbers: list[int], target: int) -> list[int]|None:
    # O(n)
    numbers_dict = {}
    for i, number in enumerate(numbers):
        complement = target - number
        if complement in numbers_dict:
            return [i, numbers_dict[complement]]
        numbers_dict[number] = i




def main():
    a = most_frequent([1, 2, 2, 3, 3, 3, 4])
    a = most_frequent([7])
    a = most_frequent([])
    a = count_pairs_with_diff([1, 7, 5, 9, 2, 12, 3], k=2)
    a = count_pairs_with_diff([1, 7, 5, 9, 2, 12, 3], k=20)
    a = count_pairs_with_diff([1], k=2)
    a = count_pairs_with_diff([], k=2)
    a = two_sum([2, 7, 11, 15], target=9)
    print()


if __name__ == "__main__":
    main()
