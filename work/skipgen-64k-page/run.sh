#!/bin/sh

set -ex

if [ ! -f rpb-console-image-lkft-juno-20190222182022.rootfs.tar ]; then
    wget http://people.linaro.org/~daniel.diaz/arm-64kpages/rpb-console-image-lkft-juno-20190222182022.rootfs.tar.xz
    unxz rpb-console-image-lkft-juno-20190222182022.rootfs.tar.xz
fi

qemu-system-x86_64 \
    -cpu host \
    -enable-kvm \
    -nographic \
    -m 1024 \
    -monitor none \
    -drive format=raw,file=rpb-console-image-lkft-juno-20190222182022.rootfs.tar,if=virtio \
    -m 4096 \
    -smp 4 \
    -nographic

    #-net nic,model=virtio,macaddr=DE:AD:BE:EF:66:09 \
    #-net tap \
    #-drive format=qcow2,file=/var/lib/lava/dispatcher/tmp/512985/apply-overlay-guest-zhxbtjts/lava-guest.qcow2,media=disk,if=virtio

