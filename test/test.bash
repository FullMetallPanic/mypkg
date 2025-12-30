#!/bin/bash
# SPDX-FileCopyrightText: 2025 Hayato Matsumoto
# SPDX-License-Identifier: BSD-3-Clause

set -e
RESULT=0

WS_DIR=~/ros2_ws
[ "$1" != "" ] && WS_DIR="$1"

cd "$WS_DIR"
source install/setup.bash


timeout 10 ros2 run mypkg poker_dealer > /tmp/dealer.log 2> /tmp/dealer.err &
DEALER_PID=$!


sleep 2
ros2 topic echo --once /poker_table > /tmp/poker_table.log || RESULT=1


kill $DEALER_PID
sleep 1


grep -q '"hole": \[' /tmp/poker_table.log || RESULT=1
grep -q '"community": \[' /tmp/poker_table.log || RESULT=1


python3 - <<EOF || RESULT=1
import json
with open("/tmp/poker_table.log") as f:
    data = json.load(f)
    assert "hole" in data and "community" in data
    assert len(data["hole"]) == 2
    assert len(data["community"]) == 5
EOF


grep -q 'Deal:' /tmp/dealer.log || RESULT=1


exit $RESULT
