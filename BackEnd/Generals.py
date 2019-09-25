from typing import List


def return_first_difference_of_one_in_sets_or_none(pre_operator_sets: List[set], post_operator_sets: List[set]):
    """
    Subtraction operation difference between pre and pos operator.
    :param pre_operator_sets: PRE - pos
    :param post_operator_sets: pre - POS
    :return: one object of pre_operator_set (difference) or None
    """
    for pre_operator_set in pre_operator_sets:
        for post_operator_set in post_operator_sets:
            difference = pre_operator_set - post_operator_set
            if len(difference) == 1:
                return difference.pop()
    return None


def return_list_of_set_which_no_have_objects_present_in_set(objects_set: set, list_of_objects_set: List[set]) -> List:
    """
    Clean sets, with object present filter
    :param objects_set: list of objects fot filter
    :param list_of_objects_set: list of set with object to be filtered
    :return: new list, with sets which no have object present in objects_set
    """
    new_list_of_objects_set = []
    for obj_set in list_of_objects_set:
        append = True
        for obj in objects_set:
            if obj in obj_set:
                append = False
                break
        if append:
            new_list_of_objects_set.append(obj_set)
    return new_list_of_objects_set


def return_one_object_in_a_set_present_in_difference_with_one_of_the_list_where_difference_size_is_lower(
        pre_operator_sets: List[set], post_operator_set: set):
    """
    Take one object from the first set of the list, like difference with the no list set (no zero) is the minor
    :param pre_operator_sets: List of sets from take a object
    :param post_operator_set: Set of object for filter the list
    :return: One object of the minor difference
    """
    lower_difference_len = len(pre_operator_sets[0])
    object_to_return = None
    for pre_operator_set in pre_operator_sets:
        difference = pre_operator_set - post_operator_set
        if len(difference) and len(difference) < lower_difference_len:
            lower_difference_len = len(difference)
            object_to_return = difference.pop()
    return object_to_return
