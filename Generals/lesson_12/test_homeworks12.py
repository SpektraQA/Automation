import unittest
from homeworks import count_trees, calculate_perimeter, count_children


# task 1: calculate_perimeter
class TestCalculatePerimeter(unittest.TestCase):
    def test_square(self):
        self.assertEqual(20, calculate_perimeter(5, 5, 5, 5))

    def test_rectangle(self):
        self.assertEqual(26, calculate_perimeter(3, 10, 3, 10))

    def test_square_is_zero(self):
        self.assertEqual(0, calculate_perimeter(0, 0, 0, 0))

    def test_square_is_digits(self):
        self.assertEqual(10.0, calculate_perimeter(2.5, 2.5, 2.5, 2.5))

# task 2: count_trees
class TestCountTrees(unittest.TestCase):
    def test_value(self):
        self.assertEqual(15, count_trees())

    def test_is_int(self):
        self.assertIsInstance(count_trees(), int)

    def test_bigger(self):
        self.assertGreater(count_trees(), 0)

    def test_not_equal(self):
        self.assertNotEqual(0, count_trees())

# task 4: count_children
class TestCalculateChildren(unittest.TestCase):
    def test_is_true(self):
        self.assertTrue(count_children())

    def test_Less_Equal(self):
        self.assertLessEqual(count_children(), 36)


if __name__ == "__main__":
    unittest.main()