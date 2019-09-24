from typing import List, Set

from BackEnd.StaticDataBase import win_sets
from BackEnd.Generals import return_first_difference_of_one_in_sets_or_none as get_win_position


class ComputerIA:
    @staticmethod
    def try_win(positions_taken: List[Set[str]]):
        """
        If can win, then win.
        Check if have almost one win set from need only one.
        :return: position to take or None
        """
        return get_win_position(win_sets, positions_taken)

    @staticmethod
    def move():
        try_win()
