from typing import Set

from BackEnd.StaticDataBase import win_sets, center_position
from BackEnd.Generals import return_first_difference_of_one_in_sets_or_none as get_win_position, \
    return_list_of_set_which_no_have_objects_present_in_set as filter_no_possible_win_sets, \
    return_one_object_in_a_set_present_in_difference_with_one_of_the_list_where_difference_size_is_lower as general_move


class ComputerIA:
    def __init__(self, positions_taken: Set[str], rival_positions_taken: Set[str]):
        self.positions_taken = positions_taken
        self.rival_positions_taken = rival_positions_taken

    def move(self) -> str:
        types_of_movements = ('win', 'defend')
        for move_type in types_of_movements:
            position_to_take = self.try_move_for(move_type)
            if position_to_take:
                return position_to_take
        # Try take center position
        if center_position not in self.positions_taken.union(self.rival_positions_taken):
            return center_position
        # Take a second place in line or any place
        # @TODO here can make better plays:
        available_win_sets = filter_no_possible_win_sets(self.rival_positions_taken, win_sets)
        position_to_take = general_move(win_sets, self.positions_taken)
        if position_to_take:
            return position_to_take
        raise Exception('Are needed available positions to play')

    def try_move_for(self, intention: str) -> str:
        if intention == 'win':
            positions_set = self.positions_taken
            available_win_sets = filter_no_possible_win_sets(self.rival_positions_taken, win_sets)
        elif intention == 'defend':
            positions_set = self.rival_positions_taken
            available_win_sets = filter_no_possible_win_sets(self.positions_taken, win_sets)
        else:
            raise ValueError('bad move intention: %s' % intention)
        take_position = get_win_position(available_win_sets, [positions_set])
        return take_position
