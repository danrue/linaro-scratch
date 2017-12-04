#!/bin/sh
set -x

# /opt/ltp/testcases/bin/madvise09

cp /boot/config-4.14.0-250-arm64 .config
yes "" | make oldconfig

make clean
make -j40 || exit 125 # git bisect skip

# copy to second host
# install to second host
  # make modules_install install
# reboot second host
# wait for second host to come online
# run test, exit accordingly


