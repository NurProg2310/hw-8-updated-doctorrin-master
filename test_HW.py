import unittest
import HW


class TestExercises(unittest.TestCase):
    def test_count_unique_elements(self):
        self.assertEqual(HW.count_unique_elements([1, 2, 3, 1, 2, 4, 5, 4]), 5)
        self.assertEqual(HW.count_unique_elements([]), 0)
        self.assertEqual(HW.count_unique_elements([1, 1, 1, 1]), 1)
        self.assertEqual(HW.count_unique_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 10)
        self.assertEqual(HW.count_unique_elements([1, 1, 2, 2, 3, 3, 4, 4]), 4)

    def test_remove_duplicates(self):
        self.assertEqual(HW.remove_duplicates([1, 2, 3, 1, 2, 4, 5, 4]), [1, 2, 3, 4, 5])
        self.assertEqual(HW.remove_duplicates([]), [])
        self.assertEqual(HW.remove_duplicates([1, 1, 1, 1]), [1])
        self.assertEqual(HW.remove_duplicates([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(HW.remove_duplicates([1, 1, 2, 2, 3, 3, 4, 4]), [1, 2, 3, 4])

    def test_reverse_list(self):
        self.assertEqual(HW.reverse_list([1, 2, 3, 4, 5]), [5, 4, 3, 2, 1])
        self.assertEqual(HW.reverse_list([]), [])
        self.assertEqual(HW.reverse_list([1]), [1])
        self.assertEqual(HW.reverse_list([1, 2]), [2, 1])
        self.assertEqual(HW.reverse_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [10, 9, 8, 7, 6, 5, 4, 3, 2, 1])

    def test_max_value(self):
        self.assertEqual(HW.max_value([1, 2, 3, 4, 5]), 5)
        self.assertEqual(HW.max_value([1]), 1)
        self.assertEqual(HW.max_value([-1, -2, -3, -4, -5]), -1)
        self.assertEqual(HW.max_value([1, 1, 1, 1]), 1)
        self.assertEqual(HW.max_value([10**6]*10), 10**6)

    def test_min_value(self):
        self.assertEqual(HW.min_value([1, 2, 3, 4, 5]), 1)
        self.assertEqual(HW.min_value([1]), 1)
        self.assertEqual(HW.min_value([-1, -2, -3, -4, -5]), -5)

    def test_sum_values(self):
        self.assertEqual(HW.sum_values([1, 2, 3, 4, 5]), 15)
        self.assertEqual(HW.sum_values([1]), 1)
        self.assertEqual(HW.sum_values([-1, -2, -3, -4, -5]), -15)
        self.assertEqual(HW.sum_values([1, 1, 1, 1]), 4)
        self.assertEqual(HW.sum_values([10**6]*10**6), 10**12)

    def test_average(self):
        self.assertEqual(HW.average([1, 2, 3, 4, 5]), 3.0)
        self.assertEqual(HW.average([1]), 1.0)
        self.assertEqual(HW.average([-1, -2, -3, -4, -5]), -3.0)
        self.assertEqual(HW.average([1, 1, 1, 1]), 1.0)
        self.assertEqual(HW.average([10**6]*10**6), 10**6)

    def test_find_index(self):
        self.assertEqual(HW.find_index([1, 2, 3, 4, 5], 3), 2)
        self.assertEqual(HW.find_index([1, 2, 3, 4, 5], 6), -1)
        self.assertEqual(HW.find_index([], 1), -1)
        self.assertEqual(HW.find_index([1, 1, 1, 1], 1), 0)
        self.assertEqual(HW.find_index([1, 2, 3, 4, 5], 1), 0)

    def test_is_sorted(self):
        self.assertTrue(HW.is_sorted([1, 2, 3, 4, 5]))
        self.assertFalse(HW.is_sorted([1, 3, 2, 4, 5]))
        self.assertTrue(HW.is_sorted([]))
        self.assertTrue(HW.is_sorted([1]))
        self.assertTrue(HW.is_sorted([-1, -1, 0, 1, 2]))

    def test_count_frequency(self):
        self.assertEqual(HW.count_frequency([1, 2, 3, 4, 5, 1, 2, 3], 3), 2)
        self.assertEqual(HW.count_frequency([1, 2, 3, 4, 5], 6), 0)
        self.assertEqual(HW.count_frequency([], 1), 0)
        self.assertEqual(HW.count_frequency([1, 1, 1, 1], 1), 4)
        self.assertEqual(HW.count_frequency([1, 2, 3, 4, 5], 1), 1)

    def test_find_mode(self):
        self.assertEqual(HW.find_mode([1, 2, 3, 4, 5, 1, 2, 2, 3]), 2)
        self.assertEqual(HW.find_mode([1]), 1)
        self.assertEqual(HW.find_mode([]), None)
        self.assertEqual(HW.find_mode([1, 2, 3]), 1)
        self.assertEqual(HW.find_mode([1, 1, 1, 2, 2]), 1)

    def test_remove_all(self):
        self.assertEqual(HW.remove_all([1, 2, 3, 4, 5, 1, 2, 3], 3), [1, 2, 4, 5, 1, 2])
        self.assertEqual(HW.remove_all([], 1), [])
        self.assertEqual(HW.remove_all([1, 1, 1, 1], 1), [])
        self.assertEqual(HW.remove_all([1, 2, 3], 4), [1, 2, 3])

    def test_rotate_left(self):
        self.assertEqual(HW.rotate_left([1, 2, 3, 4, 5], 2), [3, 4, 5, 1, 2])
        self.assertEqual(HW.rotate_left([], 1), [])
        self.assertEqual(HW.rotate_left([1], 1), [1])
        self.assertEqual(HW.rotate_left([1, 2], 1), [2, 1])
        self.assertEqual(HW.rotate_left([1, 2, 3, 4, 5], 5), [1, 2, 3, 4, 5])

    def test_rotate_right(self):
        self.assertEqual(HW.rotate_right([1, 2, 3, 4, 5], 2), [4, 5, 1, 2, 3])
        self.assertEqual(HW.rotate_right([], 1), [])
        self.assertEqual(HW.rotate_right([1], 1), [1])
        self.assertEqual(HW.rotate_right([1, 2], 1), [2, 1])
        self.assertEqual(HW.rotate_right([1, 2, 3, 4, 5], 5), [1, 2, 3, 4, 5])

    def test_find_intersection(self):
        self.assertEqual(HW.find_intersection([1, 2, 3, 4], [3, 4, 5, 6]), [3, 4])
        self.assertEqual(HW.find_intersection([], []), [])
        self.assertEqual(HW.find_intersection([1], [2]), [])
        self.assertEqual(HW.find_intersection([1, 2, 3], [3, 4, 5]), [3])
        self.assertEqual(HW.find_intersection([1, 1, 1, 1], [1, 1, 1, 1]), [1])

    def test_find_union(self):
        self.assertEqual(HW.find_union([1, 2, 3, 4], [3, 4, 5, 6]), [1, 2, 3, 4, 5, 6])
        self.assertEqual(HW.find_union([], []), [])
        self.assertEqual(HW.find_union([1], [2]), [1, 2])
        self.assertEqual(HW.find_union([1, 2, 3], [3, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(HW.find_union([1, 1, 1, 1], [1, 1, 1, 1]), [1])

    def test_find_difference(self):
        self.assertEqual(HW.find_difference([1, 2, 3, 4], [3, 4, 5, 6]), [1, 2])
        self.assertEqual(HW.find_difference([], []), [])
        self.assertEqual(HW.find_difference([1], [2]), [1])
        self.assertEqual(HW.find_difference([1, 2, 3], [3, 4, 5]), [1, 2])


if __name__ == '__main__':
    unittest.main()
