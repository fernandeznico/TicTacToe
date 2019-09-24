from typing import Set

from BackEnd.StaticDataBase import win_sets
from BackEnd.Generals import return_first_difference_of_one_in_sets_or_none as get_win_position


class ComputerIA:
    def __init__(self, positions_taken: Set[str], rival_positions_taken: Set[str]):
        self.positions_taken = positions_taken
        self.rival_positions_taken = rival_positions_taken

    def try_move_for(self, intention: str):
        if intention == 'win':
            positions_set = self.positions_taken
        elif intention == 'defend':
            positions_set = self.rival_positions_taken
        else:
            raise ValueError('intention need be "win" or "defend" not "%s"' % intention)
        take_position = get_win_position(win_sets, [positions_set])
        return take_position

    def move(self):
        self.try_move_for('win')
        self.try_move_for('defend')

