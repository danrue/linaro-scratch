qemu-system-aarch64 \
  -cpu cortex-a57 \
  -machine virt \
  -nographic \
  -monitor none \
  -kernel Image--4.16+git0+d804f93aa2-r0-hikey-20180427152124-17.bin \
  --append "console=ttyAMA0 root=/dev/vda rw" \
  -drive rpb-console-image-hikey-20180427152124-17.rootfs.ext4,if=virtio \
  -m 4096 \
  -smp 4 \
  -nographic

  #-drive rpb-console-image-hikey-20180427152124-17.rootfs.ext4,if=virtio \
