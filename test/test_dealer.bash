#!/bin/bash
# SPDX-FileCopyrightText: 2025 Hayato Matsumoto
# SPDX-License-Identifier: BSD-3-Clause
set -e

source /opt/ros/humble/setup.bash
source install/setup.bash


ros2 run mypkg dealer &
DEALER_PID=$!


sleep 3


if ! ros2 topic echo --once /poker_table; then
    echo "WARNING: /poker_table not published"
    kill $DEALER_PID || true
    exit 1
fi


kill $DEALER_PID
