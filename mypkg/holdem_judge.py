#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2025 Hayato Matsumoto
# SPDX-License-Identifier: BSD-3-Clause

from itertools import combinations


RANK_ORDER = "23456789TJQKA"


def cv(card):
    r = card[:-1]
    if r == "10":
        r = "T"
    return RANK_ORDER.index(r)


def is_flush(cards):
    return len(set(c[-1] for c in cards)) == 1


def is_straight(cards):
    vals = sorted(set(cv(c) for c in cards))

    if len(vals) == 5 and max(vals) - min(vals) == 4:
        return True

    # Wheel Straight (A 2 3 4 5)
    if set(vals) == {12, 0, 1, 2, 3}:
        return True

    return False


def hand_rank(cards):
    ranks = [c[:-1] for c in cards]
    cnt = {r: ranks.count(r) for r in ranks}
    v = sorted(cnt.values(), reverse=True)

    if is_straight(cards) and is_flush(cards):
        return "Straight Flush"
    if 4 in v:
        return "Four of a Kind"
    if 3 in v and 2 in v:
        return "Full House"
    if is_flush(cards):
        return "Flush"
    if is_straight(cards):
        return "Straight"
    if 3 in v:
        return "Three of a Kind"
    if v.count(2) == 2:
        return "Two Pair"
    if 2 in v:
        return "One Pair"
    return "High Card"


ORDER = [
    "High Card",
    "One Pair",
    "Two Pair",
    "Three of a Kind",
    "Straight",
    "Flush",
    "Full House",
    "Four of a Kind",
    "Straight Flush"
]


def evaluate_best_hand(cards7):
    best = "High Card"
    for comb in combinations(cards7, 5):
        h = hand_rank(list(comb))
        if ORDER.index(h) > ORDER.index(best):
            best = h
    return best
