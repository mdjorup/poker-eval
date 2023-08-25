from itertools import product

from utils import get_prime, has_5_set_bits


def construct_flush_lookup():
    # straight flushes
    flush_lookup = {}
    i = 0x1f00
    score = 1
    while i >= 0x001f:
        flush_lookup[i] = score
        score += 1
        i >>= 1
    flush_lookup[0x100f] = score

    i = 0x1f00
    score = 323
    while i >= 0x001f:
        if flush_lookup.get(i) or not has_5_set_bits(i):
            i -= 1
            continue
        flush_lookup[i] = score
        i -= 1
        score += 1

    return flush_lookup

def construct_unique_5_lookup():
    lookup = {}
    i = 0x1f00
    score = 1600
    while i >= 0x001f:
        lookup[i] = score
        score += 1
        i >>= 1
    lookup[0x100f] = score

    i = 0x1f00
    score = 6186
    while i >= 0x001f:
        if lookup.get(i) or not has_5_set_bits(i):
            i -= 1
            continue
        lookup[i] = score
        i -= 1
        score += 1
    return lookup

def construct_4_kind_lookup():
    lookup = {}
    score = 11
    four_kind_rank = 12
    while four_kind_rank >= 0:
        kicker_rank = 12
        while kicker_rank >= 0:
            if kicker_rank == four_kind_rank:
                kicker_rank -= 1
                continue
            i = get_prime(four_kind_rank) ** 4 * get_prime(kicker_rank)
            lookup[i] = score
            score += 1
            kicker_rank -= 1
        four_kind_rank -= 1
    return lookup

def construct_full_house_lookup():
    lookup = {}
    score = 167
    three_kind_rank = 12
    while three_kind_rank >= 0:
        two_kind_rank = 12
        while two_kind_rank >= 0:
            if two_kind_rank == three_kind_rank:
                two_kind_rank -= 1
                continue
            i = get_prime(three_kind_rank) ** 3 * get_prime(two_kind_rank) ** 2
            lookup[i] = score
            score += 1
            two_kind_rank -= 1
        three_kind_rank -= 1
    return lookup

def construct_3_kind_lookup():
    lookup = {}
    score = 1610
    for (three_kind_rank, a, b) in product(range(12, -1, -1), repeat=3):
        if a == three_kind_rank or b == three_kind_rank or a == b:
            continue
        prime_multiple = get_prime(three_kind_rank) ** 3 * get_prime(a) * get_prime(b)
        if lookup.get(prime_multiple):
            continue
        lookup[prime_multiple] = score
        score += 1
    return lookup

def construct_2_pair_lookup():
    lookup = {}
    score = 2468
    for (pair1, pair2, a) in product(range(12, -1, -1), repeat=3):
        if pair1 == pair2 or pair1 == a or pair2 == a:
            continue
        prime_multiple = get_prime(pair1) ** 2 * get_prime(pair2) ** 2 * get_prime(a)
        if lookup.get(prime_multiple):
            continue
        lookup[prime_multiple] = score
        score += 1
    return lookup

def construct_pair_lookup():
    lookup = {}
    score = 3326
    for (pair, a, b, c) in product(range(12, -1, -1), repeat=4):
        if pair == a or pair == b or pair == c or a == b or a == c or b == c:
            continue
        prime_multiple = get_prime(pair) ** 2 * get_prime(a) * get_prime(b) * get_prime(c)
        if lookup.get(prime_multiple):
            continue
        lookup[prime_multiple] = score
        score += 1
    return lookup

def construct_other_lookup():
    # 4 of a kind
    lookup = {}
    
    four_kind_lookup = construct_4_kind_lookup()
    full_house_lookup = construct_full_house_lookup()
    three_kind_lookup = construct_3_kind_lookup()
    two_pair_lookup = construct_2_pair_lookup()
    pair_lookup = construct_pair_lookup()
    lookup.update(four_kind_lookup)
    lookup.update(full_house_lookup)
    lookup.update(three_kind_lookup)
    lookup.update(two_pair_lookup)
    lookup.update(pair_lookup)


    return lookup

def construct_lookup():
    flush_lookup = construct_flush_lookup()
    unique_5 = construct_unique_5_lookup()
    other_lookup = construct_other_lookup()
    return flush_lookup, unique_5, other_lookup


