#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2025 Hayato Matsumoto
# SPDX-License-Identifier: BSD-3-Clause

import sys
import json
from itertools import combinations

RANK_ORDER = "23456789TJQKA"

def card_value(card):
    r = card[:-1]
    if r == "10":
        r = "T"
    return RANK_ORDER.index(r)

def is_flush(cards):
    suits = [c[-1] for c in cards]
    return len(set(suits)) == 1

def is_straight(cards):
    values = sorted([card_value(c) for c in cards])
    values = sorted(set(values))
    if len(values) < 5:
        return False
    return max(values) - min(values) == 4

def hand_rank(cards):
    ranks = [card[:-1] for c in cards]
    counts = {r: ranks.count(r) for r in ranks}
    count_values = sorted(counts.values(), reverse=True)

    if is_straight(cards) and is_flush(cards):
        return (8, "Straight Flush")
    if 4 in count_values:
        return (7, "Four of a Kind")
    if 3 in count_values and 2 in count_values:
        return (6, "Full House")
    if is_flush(cards):
        return (5, "Flush")
    if is_straight(cards):
        return (4, "Straight")
    if 3 in count_values:
        return (3, "Three of a Kind")
    if count_values.count(2) == 2:
        return (2, "Two Pair")
    if 2 in count_values:
        return (1, "One Pair")
    return (0, "High Card")

def best_hand(hole, community):
    cards = hole + community
    best = (-1, "Unknown")
    for comb in combinations(cards, 5):
        rank = hand_rank(list(comb))
        if rank[0] > best[0]:
            best = rank
    return best

text = sys.stdin.read()

try:
    data = json.loads(text)
except:
    print("Invalid input format", file=sys.stderr)
    sys.exit(1)

hole = data["hole"]
community = data["community"]

rank_value, name = best_hand(hole, community)

print("Texas Hold'em Hand Evaluator\n")
print("Hole Cards:", " ".join(hole))
print("Community:", " ".join(community))
print(f"\nBest Hand: {name}")
print("Strength Score:", rank_value * 10)

sys.exit(0)

