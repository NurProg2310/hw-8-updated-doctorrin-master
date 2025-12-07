def longest_consecutive(my_list: list[int]) -> int:
    if not my_list:
        return 0
    nums = set(my_list)
    longest = 0
    for x in nums:
        if x - 1 not in nums:
            length = 1
            while x + length in nums:
                length += 1
            longest = max(longest, length)
    return longest


def find_missing(my_list: list[int]) -> int:
    n = len(my_list) + 1
    return n * (n + 1) // 2 - sum(my_list)


def find_duplicate(my_list: list[int]):
    seen = set()
    for num in my_list:
        if num in seen:
            return num
        seen.add(num)
    return None

def group_anagrams(words: list[str]) -> list[list[str]]:
    groups = {}
    for word in words:
        key = tuple(sorted(word))
        groups.setdefault(key, []).append(word)
    return list(groups.values())
