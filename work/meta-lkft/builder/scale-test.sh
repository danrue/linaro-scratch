#!/bin/sh

set -x

for i in `ls user-data-*`; do
    ./build.py $i &
done;
wait
