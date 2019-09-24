import unittest


class GeneralsTest(unittest.TestCase):
    def test_return_first_difference_of_one_in_sets_or_none(self):
        from BackEnd.Generals import return_first_difference_of_one_in_sets_or_none
        self.assertEqual(return_first_difference_of_one_in_sets_or_none([{'a'}], [{'b'}]), 'a')

    def test_return_list_of_set_which_no_have_objects_present_in_set(self):
        from BackEnd.Generals import return_list_of_set_which_no_have_objects_present_in_set
        self.assertEqual(return_list_of_set_which_no_have_objects_present_in_set({'a'}, [{'a'}, {'b'}]), [{'b'}])


if __name__ == '__main__':
    unittest.main()
