import unittest


class GeneralsTest(unittest.TestCase):
    def test_return_first_difference_of_one_in_sets_or_none(self):
        from BackEnd.Generals import return_first_difference_of_one_in_sets_or_none
        self.assertEqual(return_first_difference_of_one_in_sets_or_none([{'a'}], [{'b'}]), 'a')


if __name__ == '__main__':
    unittest.main()
