#!/bin/bash
set -e

ws=~
[ "$1" != "" ] && ws="$1"

cd "$ws" || exit 1

colcon build
source install/setup.bash

timeout 10 ros2 launch mypkg talk_listen.launch.py > /tmp/mypkg.log

cat /tmp/mypkg.log | grep "Poker Listener Started"
