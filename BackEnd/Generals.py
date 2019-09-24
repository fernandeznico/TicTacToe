from typing import List, Set


def return_first_difference_of_one_in_sets_or_none(pre_operator_sets: List[set], post_operator_sets: List[set]) -> str:
    """
    Subtraction operation difference between pre and pos operator.
    :param pre_operator_sets: PRE - pos
    :param post_operator_sets: pre - POS
    :return: one object of pre_operator_set (difference) or '' (empty string)
    """
    for pre_operator_set in pre_operator_sets:
        for post_operator_set in post_operator_sets:
            difference = pre_operator_set - post_operator_set
            if len(difference) == 1:
                return difference.pop()
    return ''


def return_list_of_set_which_no_have_objects_present_in_set(objects_set: set, list_of_objects_set: List[set]) -> List:
    """
    Clean sets, with object present filter
    :param objects_set: list of objects fot filter
    :param list_of_objects_set: list of set with object to be filtered
    :return: new list, with sets which no have object present in objects_set
    """
    new_list_of_objects_set = []
    for obj in objects_set:
        for obj_set in list_of_objects_set:
            if obj not in obj_set:
                new_list_of_objects_set.append(obj_set)
    return new_list_of_objects_set
