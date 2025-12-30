#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2025 Hayato Matsumoto
# SPDX-License-Identifier: BSD-3-Clause
from mypkg.holdem_judge import evaluate_best_hand
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import json

class PokerJudge(Node):
    def __init__(self):
        super().__init__("poker_judge")
        self.sub = self.create_subscription(String, "/poker_table", self.callback, 10)
        self.pub = self.create_publisher(String, "/poker_result", 10)
        self.get_logger().info("Poker Judge Started")

    def callback(self, msg):
        data = json.loads(msg.data)
        hole = data["hole"]
        community = data["community"]

        best = evaluate_best_hand(hole + community)

        out = {
            "hole": hole,
            "community": community,
            "result": best
        }

        rosmsg = String()
        rosmsg.data = json.dumps(out)

        self.pub.publish(rosmsg)
        self.get_logger().info(f"Judged: {rosmsg.data}")

def main():
    rclpy.init()
    node = PokerJudge()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()

