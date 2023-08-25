import argparse

from evaluate import simulate_n
from utils import card_to_int

parser = argparse.ArgumentParser(
                    prog='Poker Evaluator',
                    description='This program can evaluate your Texas Hold\'em poker hand and assign a win probability to it.')

parser.add_argument("c1", help="Card 1. Must be in the format [rank][suit]. For example: TC = 10 of clubs.", type=str)
parser.add_argument("c2", help="Card 2. Must be in the format [rank][suit]. For example: TC = 10 of clubs.", type=str)
parser.add_argument("n_players", help="The number of players in the hand, including yourself", type=int)

args = parser.parse_args()

c1, c2, n_players = args.c1, args.c2, args.n_players

c1_int = card_to_int(c1)
c2_int = card_to_int(c2)

win_prob, error_margin = simulate_n(10000, c1_int, c2_int, n_players)

print(f"Win probability: {win_prob * 100:.2f}% ± {error_margin * 100:.2f}%")

exit(0)

