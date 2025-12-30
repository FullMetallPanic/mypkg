#!/bin/bash
# SPDX-FileCopyrightText: 2025 Hayato Matsumoto
# SPDX-License-Identifier: BSD-3-Clause

set -e
RESULT=0

WS_DIR=~/ros2_ws
[ "$1" != "" ] && WS_DIR="$1"

cd "$WS_DIR"
colcon build --event-handlers console_direct+ > /tmp/build.log 2>&1 || RESULT=1
source "$WS_DIR/install/setup.bash"


timeout 10 ros2 run mypkg poker_dealer > /tmp/dealer.log 2> /tmp/dealer.err &
DEALER_PID=$!
timeout 10 ros2 run mypkg poker_judge > /tmp/judge.log 2> /tmp/judge.err &
JUDGE_PID=$!

sleep 3
ros2 topic echo --once /poker_result > /tmp/poker_result.log || RESULT=1

kill $DEALER_PID $JUDGE_PID
sleep 1

grep -q '"hole": \[' /tmp/poker_result.log || RESULT=1
grep -q '"community": \[' /tmp/poker_result.log || RESULT=1
grep -q '"result":' /tmp/poker_result.log || RESULT=1

python3 - <<EOF || RESULT=1
import json
with open("/tmp/poker_result.log") as f:
    data = json.load(f)
    assert len(data["hole"]) == 2
    assert len(data["community"]) == 5
    assert "result" in data
EOF

exit $RESULT
