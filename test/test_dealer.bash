#!/bin/bash
# SPDX-FileCopyrightText: 2025 Hayato Matsumoto
# SPDX-License-Identifier: BSD-3-Clause

set -e

WS_DIR="$1"
[ "$WS_DIR" == "" ] && WS_DIR=~/ros2_ws


source /opt/ros/humble/setup.bash
if [ -f "$WS_DIR/install/setup.bash" ]; then
    source "$WS_DIR/install/setup.bash"
else
    echo "ERROR: $WS_DIR/install/setup.bash not found"
    exit 1
fi

cd "$WS_DIR"


ros2 run mypkg dealer > /tmp/dealer.log 2> /tmp/dealer.err &
DEALER_PID=$!


sleep 3


if ! ros2 topic echo --once /poker_table > /tmp/poker_table.log 2>/tmp/poker_table.err; then
    echo "WARNING: /poker_table not published"
    kill $DEALER_PID || true
    wait $DEALER_PID 2>/dev/null || true
    exit 1
fi


kill $DEALER_PID || true
wait $DEALER_PID 2>/dev/null || true
