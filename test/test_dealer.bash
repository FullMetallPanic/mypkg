#!/bin/bash
# SPDX-FileCopyrightText: 2025 Hayato Matsumoto
# SPDX-License-Identifier: BSD-3-Clause

set -e

WS_DIR=${1:-$HOME/ros2_ws}

cd "$WS_DIR"
colcon build --event-handlers console_direct+

source install/setup.bash

timeout 10 ros2 run mypkg poker_dealer &
DEALER_PID=$!

sleep 2

timeout 10 bash -c "source install/setup.bash && ros2 topic echo --once /poker_table"

if ps -p $DEALER_PID > /dev/null 2>&1; then
    kill $DEALER_PID
fi
