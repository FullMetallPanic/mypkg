#!/bin/bash
# SPDX-FileCopyrightText: 2025 Hayato Matsumoto
# SPDX-License-Identifier: BSD-3-Clause

set -e

RESULT=0
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
ros2 run mypkg judge > /tmp/judge.log 2> /tmp/judge.err &
JUDGE_PID=$!

sleep 3

ros2 topic echo --once /poker_table > /tmp/poker_table.log 2>/tmp/poker_table.err || RESULT=1
ros2 topic echo --once /poker_result > /tmp/poker_result.log 2>/tmp/poker_result.err || RESULT=1


for pid in $DEALER_PID $JUDGE_PID; do
    if ps -p $pid > /dev/null 2>&1; then
        kill $pid
    fi
    wait $pid 2>/dev/null || true
done

exit $RESULT
