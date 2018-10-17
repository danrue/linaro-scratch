# extract tar
mkdir rootfs
sudo tar xpf rpb-console-image-am57xx-evm-20180423192219-12.rootfs.tar.xz -C rootfs/

# add init script for test
# build kernel
drue@xps:~/src/linux/mainline$ build-kernel -c -m am57xx-evm -k linux-mainline

# Also had to make uImage for x15 rootfs:
drue@xps:~/src/linux/mainline$ make -j 4 CROSS_COMPILE=arm-linux-gnueabihf- ARCH=arm KDIR=/home/drue/src/linux/mainline O=/home/drue/ragnar-artifacts/build_output/arm/v4.15-3279-g7b1cd95d65eb uImage LOADADDR=0x80008000


# copy kernel to tar
sudo cp /home/drue/ragnar-artifacts/staging/arm/v4.15-3279-g7b1cd95d65eb/zImage-v4.15-3279-g7b1cd95d65eb rootfs/boot/
sudo cp -r /home/drue/ragnar-artifacts/staging/arm/v4.15-3279-g7b1cd95d65eb/lib/modules/4.15.0-03279-g7b1cd95d65eb rootfs/lib/modules/
drue@xps:~/src/linaro-scratch/qemu/3769$ sudo cp /home/drue/ragnar-artifacts/build_output/arm/v4.15-3279-g7b1cd95d65eb/arch/arm/boot/uImage rootfs/boot/uImage-v4.15-3279-g7b1cd95d65eb
sudo ln -sf zImage-v4.15-3279-g7b1cd95d65eb rootfs/boot/zImage


# make ext4 from tar
## XXX Not sure about sizing here - existing x15 image looks to be 1.2G.
rm -f rootfs.ext4 && dd if=/dev/zero of=rootfs.ext4 seek=2097152 count=120 bs=1024
sudo mkfs.ext4 rootfs.ext4 -d rootfs/

# make an img file from ext4
ext2simg -zv rootfs.ext4 v4.15-3279-g7b1cd95d65eb-rootfs.img.gz





# kernel version
root@am57xx-evm:~# uname -a
Linux am57xx-evm 4.16.5 #1 SMP Thu Apr 26 09:57:44 UTC 2018 armv7l armv7l armv7l GNU/Linux
root@am57xx-evm:~# uname -r
4.16.5




