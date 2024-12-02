from collections import Counter
from functools import cmp_to_key, cache
from itertools import product
from typing import Callable, List, Tuple

with open(f"input/year2023/day07.txt", "r") as f:
    lines = f.read().splitlines()

card_rank = "AKQJT98765432*"
hand_rank: List[Callable[[Counter], bool]] = [
    lambda hand: len(hand) == 1,  # 5 of a kind
    lambda hand: hand.most_common()[0][1] == 4,  # 4 of a kind
    lambda hand: len(hand.keys()) == 2 and hand.most_common()[0][1] == 3,  # Full house
    lambda hand: hand.most_common()[0][1] == 3,  # 3 of a kind
    lambda hand: len(hand.keys()) > 2
    and all([x[1] == 2 for x in hand.most_common()[:2]]),  # 2 pair
    lambda hand: hand.most_common()[0][1] == 2,  # One pair
    lambda _: True,  # High card
]

@cache
def get_rank(hand: str):
    hand_counts = Counter(hand)
    for i, rank_fn in enumerate(hand_rank):
        if rank_fn(hand_counts):
            return i

@cache
def get_best_hand(hand: str):
    if "*" not in hand:
        return get_rank(hand)

    max_rank = len(hand_rank)

    star_idxs = [i for i, card in enumerate(hand) if card == "*"]
    for replacements in product(*[card_rank for _ in star_idxs]):
        new_hand = str(hand)

        for replacement in replacements:
            new_hand = new_hand.replace("*", replacement, 1)
        max_rank = min(max_rank, get_rank(new_hand))
        if max_rank == 0:
            break

    return max_rank

def comp_hand(hand_1: Tuple[str, str], hand_2: Tuple[str, str]):
    hand_1_rank, hand_2_rank = get_best_hand(hand_1[0]), get_best_hand(hand_2[0])

    if hand_1_rank == hand_2_rank:
        hand_1_card, hand_2_card = hand_1[0][0], hand_2[0][0]
        i = 1
        while hand_1_card == hand_2_card and i < len(hand_1[0]):
            hand_1_card, hand_2_card = hand_1[0][i], hand_2[0][i]
            i += 1
        return card_rank.index(hand_1_card) - card_rank.index(hand_2_card)
    else:
        return hand_1_rank - hand_2_rank

def sort_hands(hands):
    return sorted(hands, key=cmp_to_key(comp_hand), reverse=True)

hands = [line.split(" ") for line in lines]
p2_hands = [(hand.replace("J", "*"), bet) for hand, bet in hands]

print(sum([(i + 1) * int(bet) for i, (_, bet) in enumerate(sort_hands(hands))]))
print(sum([(i + 1) * int(bet) for i, (_, bet) in enumerate(sort_hands(p2_hands))]))
