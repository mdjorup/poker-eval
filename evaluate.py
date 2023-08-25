import random
from itertools import combinations

from lookups import construct_lookup
from utils import construct_bit_card

flush_lookup, unique_5, other_lookup = construct_lookup()

def evaluate(c1, c2, c3, c4, c5) -> int:
    
    c1 = construct_bit_card(c1)
    c2 = construct_bit_card(c2)
    c3 = construct_bit_card(c3)
    c4 = construct_bit_card(c4)
    c5 = construct_bit_card(c5)
    
    q = (c1 | c2 | c3 | c4 | c5) >> 16
    is_flush = (c1 & c2 & c3 & c4 & c5 & 0xF000) > 0
    # flush and straight flush
    if is_flush:
        score = flush_lookup[q]
        return score
    
    # straight and high card
    if unique_5.get(q):
        return unique_5[q]
    
    
    ff = 0xff
    q = (c1 & ff) * (c2 & ff) * (c3 & ff) * (c4 & ff) * (c5 & ff)

    if other_lookup.get(q):
        return other_lookup[q]
    
    # this is a catch all, which if in some case is not caught, will return 8000
    return 8000

def generate_hands(my_hand: list[int], n_other: int):
    other_cards = [c for c in range(52) if c != my_hand[0] and c != my_hand[1]]
    
    sample = random.sample(other_cards, 5 + n_other * 2)
    board = sample[:5]
    other_hands = [sample[5 + i * 2: 5 + i * 2 + 2] for i in range(n_other)]


    return board, other_hands


def simulate(c1_int, c2_int, n_players) -> bool:
    board, hands = generate_hands([c1_int, c2_int], n_players - 1)
    my_score = 8000
    for c, d, e in combinations(board, 3):
        score = evaluate(c1_int, c2_int, c, d, e)
        if score < my_score:
            my_score = score

    for a, b in hands:
        for c, d, e in combinations(board, 3):
            score = evaluate(a, b, c, d, e)
            if score < my_score:
                return False
            
    return True


def simulate_n(n: int, c1_int, c2_int, n_players):
    wins = 0
    for _ in range(n):
        if simulate(c1_int, c2_int, n_players):
            wins += 1
            
    win_prob = wins / n
    variance = win_prob * (1 - win_prob)
    SE = (variance / n) ** 0.5
    MOE = 1.96 * SE
    
    return win_prob, MOE