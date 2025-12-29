#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2025 Hayato Matsumoto
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
import random
import json

class PokerDealer(Node):
    def __init__(self):
        super().__init__("poker_dealer")
        self.publisher = self.create_publisher(
            msg_type=rclpy.qos.qos_profile_system_default.type, 
            topic="/poker_table",
            qos_profile=10
        )
        self.timer = self.create_timer(2.0, self.deal_cards)

    def deal_cards(self):
        suits = ["S","H","D","C"]
        ranks = ["A","K","Q","J","10","9","8","7","6","5","4","3","2"]
        deck = [r+s for s in suits for r in ranks]
        random.shuffle(deck)

        hole = deck[:2]
        community = deck[2:7]

        data = {
            "hole": hole,
            "community": community
        }

        msg = json.dumps(data)
        self.get_logger().info(f"Dealt: {msg}")
        self.publisher.publish(msg)

def main():
    rclpy.init()
    node = PokerDealer()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()

