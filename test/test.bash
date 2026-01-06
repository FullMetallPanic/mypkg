#!/bin/bash

dir=~
[ "$1" != "" ] && dir="$1"

cd "$dir/ros2_ws" || exit 1

colcon build
source "$dir/.bashrc"


timeout 10 ros2 launch mypkg talk_listen.launch.py \
  > /tmp/mypkg.log 2>&1


cat /tmp/mypkg.log | grep "Texas Hold'em Result"
