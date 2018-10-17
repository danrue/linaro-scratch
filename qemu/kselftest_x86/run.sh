#sudo mount -o loop rpb-console-image-intel-core2-32-20180510195826-852.hddimg hdimg/

qemu-system-x86_64 \
    -cpu host \
    -enable-kvm \
    -monitor none \
    -drive format=raw,file=rpb-console-image-intel-core2-32-20180510195826-852.hddimg,if=virtio \
    -m 4096 \
    -smp 4 \
    -nographic

