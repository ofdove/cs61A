from hog import play, always_roll
from dice import make_test_dice
def echo(s0, s1):
    print(s0, s1)
    return echo
strat0 = lambda score, opponent: 1- opponent // 10
strat1 = always_roll(3)
s0, s1 = play(strat0, strat1, dice=make_test_dice(4, 2, 6), goal = 15, say = echo)