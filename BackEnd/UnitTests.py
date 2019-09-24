import unittest


class GeneralsTest(unittest.TestCase):
    def test_return_first_difference_of_one_in_sets_or_none(self):
        from BackEnd.Generals import return_first_difference_of_one_in_sets_or_none as f
        self.assertEqual(f([{'a'}], [{'b'}]), 'a')
        # @TODO add more cases

    def test_return_list_of_set_which_no_have_objects_present_in_set(self):
        from BackEnd.Generals import return_list_of_set_which_no_have_objects_present_in_set as f
        self.assertEqual(f({'a'}, [{'a'}, {'b'}]), [{'b'}])
        # @TODO add more cases

    def test_return_one_object_in_a_set_present_in_difference_with_one_of_the_list_where_difference_size_is_lower(self):
        from BackEnd.Generals import \
            return_one_object_in_a_set_present_in_difference_with_one_of_the_list_where_difference_size_is_lower as f
        self.assertEqual(f([{'a', 'b'}, {'b'}, {'a', 'b', 'c'}], {'b'}), 'a')
        # @TODO add more cases


if __name__ == '__main__':
    unittest.main()
