#!/bin/sh

set -ex

if [ ! -f rpb-console-image-am57xx-evm-20180426095506-16.rootfs.ext4 ]; then
    wget http://snapshots.linaro.org/openembedded/lkft/morty/am57xx-evm/rpb/linux-stable-rc-4.16/16/rpb-console-image-am57xx-evm-20180426095506-16.rootfs.ext4.gz
    gunzip rpb-console-image-am57xx-evm-20180426095506-16.rootfs.ext4.gz
fi

if [ ! -f zImage--4.16+git0+e5ce9f6879-r0-am57xx-evm-20180426095506-16.bin ]; then
    wget http://snapshots.linaro.org/openembedded/lkft/morty/am57xx-evm/rpb/linux-stable-rc-4.16/16/zImage--4.16+git0+e5ce9f6879-r0-am57xx-evm-20180426095506-16.bin
fi

qemu-system-arm \
  -cpu cortex-a15 \
  -machine virt \
  -nographic \
  -monitor none \
  -kernel /home/drue/ragnar-artifacts/staging/arm/v4.15-3279-g7b1cd95d65eb/zImage-v4.15-3279-g7b1cd95d65eb \
  --append "console=ttyAMA0 root=/dev/vda rw" \
  -drive format=raw,file=rootfs.ext4,if=virtio \
  -m 4096 \
  -smp 2 \
  -nographic

  #-kernel zImage--4.16+git0+e5ce9f6879-r0-am57xx-evm-20180426095506-16.bin \
  #-drive format=raw,file=rpb-console-image-am57xx-evm-20180426095506-16.rootfs.ext4,if=virtio \

# am57xx-evm login: root
# root@am57xx-evm:~# cd /opt/kselftests/default-in-kernel/gpio/
# root@am57xx-evm:/opt/kselftests/default-in-kernel/gpio# ./gpio-mockup.sh
# root@am57xx-evm:/opt/kselftests/default-in-kernel/gpio# ./gpio-mockup.sh
# 1.  Test dynamic allocation of gpio successful means insert gpiochip and
#     manipulate gpio pin successful
# [  272.500917] gpio_mockup: section 3 reloc 15 sym '_find_first_bit_le': relocation 28 out of range (0xbf024168 -> 0xc10dd6c8)
# skip all tests: insmod gpio-mockup failed
# root@am57xx-evm:/opt/kselftests/default-in-kernel/gpio#
