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

sleep 2


ros2 topic echo --once /poker_table > /tmp/poker_table.log || RESULT=1


kill $DEALER_PID || true

exit $RESULT
