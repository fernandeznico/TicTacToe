"""
@package db
Save game struct like win plays.
Game positions:
a | b | c
d | e | f
g | h | i
"""

win_sets = [{'a', 'b', 'c'}, {'d', 'e', 'f'}, {'g', 'h', 'i'}, {'a', 'd', 'g'}, {'b', 'e', 'h'}, {'c', 'f', 'i'},
            {'a', 'e', 'i'}, {'c', 'e', 'g'}]
