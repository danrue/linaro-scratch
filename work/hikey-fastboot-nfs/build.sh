# The following script is an example usage of combining 'fastboot boot' with a
# ramdisk as well as with an nfsroot filesystem on a hikey 620.
#
# Note that if 'fastboot boot' complains of "FAILED (remote: 'dtb not found')",
# the firmware needs to be updated.
#

set -ex

# Retrieve kernel, modules, dtb
wget -c https://storage.kernelci.org/mainline/master/v5.1-rc7/arm64/defconfig/gcc-7/modules.tar.xz
wget -c https://storage.kernelci.org/mainline/master/v5.1-rc7/arm64/defconfig/gcc-7/Image
wget -c https://storage.kernelci.org/mainline/master/v5.1-rc7/arm64/defconfig/gcc-7/dtbs/hisilicon/hi6220-hikey.dtb

# Retrieve rootfs tar (for nfs) and cpio (for ramdisk)
wget -c https://storage.kernelci.org/images/rootfs/buildroot/kci-2018.11/arm64/base/rootfs.tar.xz
wget -c https://storage.kernelci.org/images/rootfs/buildroot/kci-2018.11/arm64/base/rootfs.cpio.gz

# Retrieve mkbootimg python script
curl "https://android.googlesource.com/platform/system/core/+/master/mkbootimg/mkbootimg.py?format=TEXT" | base64 --decode > mkbootimg
chmod a+x mkbootimg

# Build a zipped image with dtb appended
gzip -fk Image
cat Image.gz hi6220-hikey.dtb > Image.gz+dtb

# Add modules to ramdisk
tar -xf modules.tar.xz
find lib/ | cpio -ov -H newc -F modules.cpio
gzip -f modules.cpio
cat rootfs.cpio.gz modules.cpio.gz > rootfs.cpio.gz+modules.cpio.gz

# Deploy rootfs.tar.xz and modules to nfs location (omitted)
# Overlay modules to nfs location (omitted)

# Create a fastboot boot image containing a ramdisk
./mkbootimg --kernel Image.gz+dtb --ramdisk rootfs.cpio.gz+modules.cpio.gz --base 0x80000000 --pagesize 2048 --cmdline 'root=/dev/ram0 init=/sbin/init rw console=tty0 console=ttyMSM0,115200n8' -o fastboot-ramdisk.img

# Create a fastboot boot image along and embed nfsroot parameters
./mkbootimg --kernel Image.gz+dtb --base 0x80000000 --pagesize 2048 --cmdline 'root=/dev/nfs nfsroot=10.0.0.5:/foo ip=dhcp rw console=tty0 console=ttyMSM0,115200n8' -o fastboot-nfs.img

# Deploy with 'fastboot boot':
#   fastboot boot fastboot-ramdisk.img
#   fastboot boot fastboot-nfs.img
