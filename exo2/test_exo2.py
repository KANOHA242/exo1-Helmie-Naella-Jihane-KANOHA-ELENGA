import unittest
from exo2 import solution

class TestSolution(unittest.TestCase):


    def test_fixed_tests_true(self):
        fixed_tests_True = (
            ("samurai", "ai"),
            ("ninja", "ja"),
            ("sensei", "i"),
            ("abc", "abc"),
            ("abcabc", "bc"),
            ("fails", "ails"),
        )

        for string, ending in fixed_tests_True:
            with self.subTest(string=string, ending=ending):
                checker = solution(string)
                self.assertTrue(checker.ends_with(ending), f"Failed for {string} and {ending}")

    def test_fixed_tests_false(self):
        fixed_tests_False = (
            ("sumo", "omo"),
            ("samurai", "ra"),
            ("abc", "abcd"),
            ("ails", "fails"),
            ("this", "fails"),
            ("spam", "eggs"),
        )

        for string, ending in fixed_tests_False:
            with self.subTest(string=string, ending=ending):
                checker = solution(string)
                self.assertFalse(checker.ends_with(ending), f"Failed for {string} and {ending}")


if __name__ == '__main__':
    unittest.main()