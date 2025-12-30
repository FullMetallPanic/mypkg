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


timeout 10 ros2 run mypkg poker_dealer > /tmp/dealer.log 2> /tmp/dealer.err &
DEALER_PID=$!
timeout 10 ros2 run mypkg poker_judge > /tmp/judge.log 2> /tmp/judge.err &
JUDGE_PID=$!

sleep 3


ros2 topic echo --once /poker_table > /tmp/poker_table.log || RESULT=1
ros2 topic echo --once /poker_result > /tmp/poker_result.log || RESULT


kill $DEALER_PID || true
kill $JUDGE_PID  || true

exit $RESULT
