#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2025 Hayato Matsumoto
# SPDX-License-Identifier: BSD-3-Clause
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import json
import random


class PokerDealer(Node):
    def __init__(self):
        super().__init__("poker_dealer")

        self.publisher = self.create_publisher(String, "/poker_table", 10)

        self.timer = self.create_timer(0.5, self.deal_cards)

        self.get_logger().info("Poker Dealer Started")

        self.deal_cards()


    def deal_cards(self):
        deck = [r + s for r in "23456789TJQKA" for s in "SHDC"]
        random.shuffle(deck)

        hole = deck[:2]
        community = deck[2:7]

        msg = {
            "hole": hole,
            "community": community
        }

        rosmsg = String()
        rosmsg.data = json.dumps(msg)

        self.publisher.publish(rosmsg)
        self.get_logger().info(f"Deal: {rosmsg.data}")


def main():
    rclpy.init()
    node = PokerDealer()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
