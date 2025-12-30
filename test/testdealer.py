#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2025 Hayato Matsumoto
# SPDX-License-Identifier: BSD-3-Clause
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import json
import time

def test_dealer_publishes():
    rclpy.init()
    node = Node("test_node")

    received = []

    def callback(msg):
        received.append(msg.data)

    sub = node.create_subscription(
        String,
        "/poker_table",
        callback,
        10
    )

    start = time.time()
    while len(received) == 0 and time.time() - start < 6:
        rclpy.spin_once(node, timeout_sec=0.2)

    node.destroy_node()
    rclpy.shutdown()

    assert len(received) > 0

    data = json.loads(received[0])
    assert "hole" in data
    assert "community" in data
    assert len(data["hole"]) == 2
    assert len(data["community"]) == 5

