#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2025 Hayato Matsumoto
# SPDX-License-Identifier: BSD-3-Clause
from mypkg.holdem_judge import evaluate_best_hand


def test_straight_flush():
    cards = ["AS", "KS", "QS", "JS", "10S", "3D", "4C"]
    assert evaluate_best_hand(cards) == "Straight Flush"


def test_full_house():
    cards = ["AH", "AD", "AC", "7S", "7D", "3C", "4D"]
    assert evaluate_best_hand(cards) == "Full House"


def test_one_pair():
    cards = ["KH", "KD", "2C", "5D", "9H", "3S", "4D"]
    assert evaluate_best_hand(cards) == "One Pair"
