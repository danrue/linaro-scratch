set -ex

#wget -c https://storage.kernelci.org/mainline/master/v5.1-rc7/arm64/defconfig/gcc-7/modules.tar.xz
#wget -c https://storage.kernelci.org/mainline/master/v5.1-rc7/arm64/defconfig/gcc-7/Image
#wget -c https://storage.kernelci.org/mainline/master/v5.1-rc7/arm64/defconfig/gcc-7/dtbs/qcom/apq8016-sbc.dtb
#wget -c https://storage.kernelci.org/images/rootfs/buildroot/kci-2018.11/arm64/base/rootfs.tar.xz

wget -c https://storage.kernelci.org/qcom-lt/integration-linux-qcomlt/v5.1-rc7-243-gb11a2b93cbb0/arm64/defconfig/gcc-7/Image
wget -c https://storage.kernelci.org/qcom-lt/integration-linux-qcomlt/v5.1-rc7-243-gb11a2b93cbb0/arm64/defconfig/gcc-7/dtbs/qcom/apq8016-sbc.dtb
wget -c https://storage.kernelci.org/qcom-lt/integration-linux-qcomlt/v5.1-rc7-243-gb11a2b93cbb0/arm64/defconfig/gcc-7/modules.tar.xz
wget -c https://snapshots.linaro.org/member-builds/qcomlt/testimages/arm64/87/initramfs-test-image-qemuarm64-20190426151441-87.rootfs.cpio.gz

curl "https://android.googlesource.com/platform/system/core/+/master/mkbootimg/mkbootimg.py?format=TEXT" | base64 --decode > mkbootimg
chmod a+x mkbootimg

gzip -fk Image
cat Image.gz apq8016-sbc.dtb > Image.gz+dtb

tar -xf modules.tar.xz
find lib/ | cpio -ov -H newc -F modules.cpio
gzip -f modules.cpio
cat initramfs-test-image-qemuarm64-20190426151441-87.rootfs.cpio.gz modules.cpio.gz > initramfs-test-image-qemuarm64-20190426151441-87.rootfs.cpio.gz+modules.cpio.gz

./mkbootimg --kernel Image.gz+dtb --ramdisk initramfs-test-image-qemuarm64-20190426151441-87.rootfs.cpio.gz+modules.cpio.gz --base 0x80000000 --pagesize 2048 --cmdline 'root=/dev/ram0 init=/sbin/init rw console=tty0 console=ttyMSM0,115200n8' -o aboot.img

#abootimg --create aboot2.img -k Image.gz+dtb -r initramfs-test-image-qemuarm64-20190426151441-87.rootfs.cpio.gz+modules.cpio.gz -c pagesize=2048 -c kerneladdr=0x80008000 -c ramdiskaddr=0x81000000 -c cmdline='root=/dev/ram0 init=/sbin/init rw console=tty0 console=ttyMSM0,115200n8'
# fastboot -s DEVICEID boot aboot_nfs.img 
