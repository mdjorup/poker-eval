from mappings import prime_mapping, rank_mapping, rank_to_int, suit_mapping


def get_prime(n):
    return prime_mapping[n]

def get_suit(card):
    return 2 ** (card // 13)

def classify_hand(c1, c2):
    rank1 = c1 % 13
    rank2 = c2 % 13
    suit1 = get_suit(c1)
    suit2 = get_suit(c2)
    small_rank = min(rank1, rank2)
    big_rank = max(rank1, rank2)
    suited = "S" if suit1 == suit2 else "O"
    return rank_mapping[small_rank] + rank_mapping[big_rank] + suited # type: ignore


def construct_bit_card(card):
    total = 0
    rank  = card % 13
    rank_encoded = 2 ** (card % 13)
    suit = get_suit(card)
    prime = get_prime(rank)
    total += rank_encoded
    total <<= 4
    total += suit
    total <<= 4
    total += rank
    total <<= 8
    total += prime
    return total

def has_5_set_bits(n):
    count = 0
    while n:
        count += 1
        n &= n - 1
        if count > 5:  # Early stopping if more than 5 bits are found
            return False
    return count == 5


def card_to_int(card: str) -> int:
    if len(card) != 2:
        raise ValueError("Card must be of length 2")
    rank, suit = card[0], card[1]

    if not rank in rank_to_int.keys():
        raise ValueError("Rank must be one of {}".format(rank_to_int.keys()))
    if not suit in suit_mapping.keys():
        raise ValueError("Suit must be one of {}".format(suit_mapping.keys()))

    rank_int = rank_to_int[rank]
    suit_int = suit_mapping[suit]
    
    card_int = suit_int * 13 + rank_int
    

    return card_int