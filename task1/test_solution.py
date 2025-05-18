import unittest

from solution import strict, sum_two


class TestStrictDecorator(unittest.TestCase):
    def test_correct_types(self):
        self.assertEqual(sum_two(2, 3), 5)

    def test_incorrect_type_first_argument(self):
        with self.assertRaises(TypeError):
            sum_two("2", 3)

    def test_incorrect_type_second_argument(self):
        with self.assertRaises(TypeError):
            sum_two(2, "3")

    def test_both_arguments_wrong_type(self):
        with self.assertRaises(TypeError):
            sum_two("2", "3")


if __name__ == "__main__":
    unittest.main()
