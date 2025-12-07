# Exercise-1
def count_unique_elements(my_list: list) -> int:
    return len(set(my_list))

# Exercise-2
def remove_duplicates(my_list: list) -> list:
    seen = set()
    result = []
    for num in my_list:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result


# Exercise-3
def reverse_list(my_list: list) -> list:
    return my_list[::-1]


# Exercise-4
def max_value(my_list: list) -> int:
    return max(my_list)


# Exercise-5
def min_value(my_list: list) -> int:
    return min(my_list)


# Exercise-6
def sum_values(my_list: list) -> int:
    return sum(my_list)


# Exercise-7
def average(my_list: list) -> float:
    return sum(my_list) / len(my_list) if my_list else 0.0


# Exercise-8
def find_index(my_list: list, element: int) -> int:
    for i, val in enumerate(my_list):
        if val == element:
            return i
    return -1


# Exercise-9
def is_sorted(my_list: list) -> bool:
    return all(my_list[i] <= my_list[i+1] for i in range(len(my_list)-1))


# Exercise-10
def count_frequency(my_list: list, element: int) -> int:
    return my_list.count(element)


# Exercise-11
def find_mode(my_list: list):
    if not my_list:
        return None

    freq = {}
    for num in my_list:
        freq[num] = freq.get(num, 0) + 1

    return max(freq, key=freq.get)

# Exercise-12
def remove_all(my_list: list, element: int) -> list:
    return [x for x in my_list if x != element]


# Exercise-13
def rotate_left(my_list: list, k: int) -> list:
    if not my_list:
        return my_list
    k %= len(my_list)
    return my_list[k:] + my_list[:k]


# Exercise-14
def rotate_right(my_list: list, k: int) -> list:
    if not my_list:
        return my_list
    k %= len(my_list)
    return my_list[-k:] + my_list[:-k]


# Exercise-15
def find_intersection(list1: list, list2: list) -> list:
    return list(set(list1) & set(list2))


# Exercise-16
def find_union(list1: list, list2: list) -> list:
    return list(set(list1) | set(list2))


# Exercise-17
def find_difference(list1: list, list2: list) -> list:
    return list(set(list1) - set(list2))
