from typing import List, Set

from BackEnd.StaticDataBase import win_sets
from BackEnd.Generals import return_first_difference_of_one_in_sets_or_none as get_win_position


class ComputerIA:
    @staticmethod
    def try_win(positions_taken: Set[str]) -> str:
        """
        If can win, then win.
        Check if have almost one win set from need only one.
        :param positions_taken: set of positions in computer possession
        :return: position to take for win or ''
        """
        return get_win_position(win_sets, [positions_taken])

    @staticmethod
    def try_defend(rival_positions_taken: List[Set[str]]) -> str:
        """
        If need cover a position, to prevent rival win, then cover.
        :param rival_positions_taken:
        :return:
        """

    @staticmethod
    def move(positions_taken: List[Set[str]]):
        take_position = ComputerIA.try_win(positions_taken)
        if take_position:
            return take_position

