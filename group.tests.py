import group
import unittest

class TestCases(unittest.TestCase):
    pass

    def test_groups_of_3_1(self):
        integers_list = [1,2,3,4,5,6,7,8,9]
        expected = [[1,2,3], [4,5,6], [7,8,9]]
        actual = group.groups_of_3(integers_list)
        self.assertEqual(expected, actual)

    def test_groups_of_3_2(self):
        integers_list = [1,2,3,4,5,6,7,8]
        expected = [[1,2,3], [4,5,6], [7,8]]
        actual = group.groups_of_3(integers_list)
        self.assertEqual(expected, actual)
