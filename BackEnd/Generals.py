from typing import List


def return_first_difference_of_one_in_sets_or_none(pre_operator_sets: List[set], post_operator_sets: List[set]):
    """
    Subtraction operation difference between pre and pos operator.
    :param pre_operator_sets: PRE - pos
    :param post_operator_sets: pre - POS
    :return: one object of pre_operator_set (difference) or none
    """
    for pre_operator_set in pre_operator_sets:
        for post_operator_set in post_operator_sets:
            difference = post_operator_set - pre_operator_set
            if len(difference) == 1:
                return difference.pop()
    return None
