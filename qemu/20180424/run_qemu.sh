ROOTFS=rpb-console-image-intel-core2-32-20180423185518-244.hddimg

if [ ! -f "${ROOTFS}" ]; then
    wget http://snapshots.linaro.org/openembedded/lkft/morty/intel-core2-32/rpb/linux-stable-rc-4.9/244/${ROOTFS}.xz
    unxz ${ROOTFS}.xz
fi

qemu-system-x86_64 \
  -cpu host \
  -enable-kvm \
  -nographic \
  -net nic,model=virtio,macaddr=DE:AD:BE:EF:66:01 \
  -monitor none \
  -drive format=raw,file=rpb-console-image-intel-core2-32-20180423185518-244.hddimg,if=virtio \
  -m 4096 \
  -smp 4 \
  -nographic

  #-append "vsyscall=native" \
  #-append "console=ttyAMA0 root=/dev/vda rw" \
  #-kernel bzImage--4.9+git0+8617c15e22-r0-intel-core2-32-20180423185518-244.bin \

