Debugging x15

# extract rootfs
mkdir rootfs; cd rootfs; sudo tar xf ../rpb...

# modify rootfs as needed
# repackage rootfs and submit lava job
drue@xps:~/src/linaro-scratch/work/x15$ (cd rootfs && sudo tar cvzf ../rootfs.tgz .) && scp rootfs.tgz people.linaro.org:~/public_html/files/ && lavacli -i therub jobs submit --url x15_uboot.yaml


# Attempts

drue@xps:~/src/linaro-scratch/work/x15/rootfs/etc/systemd/system$ rm dbus-org.freedesktop.network1.service dbus-org.freedesktop.NetworkManager.service dbus-org.
freedesktop.resolve1.service
  - no change in boot

drue@xps:~/src/linaro-scratch/work/x15/rootfs/etc/systemd/system$ sudo rm -rf network-online.target.wants/
  - no change in boot

drue@xps:~/src/linaro-scratch/work/x15/rootfs/etc/systemd/system$ sudo rm dbus-org.freedesktop.nm-dispatcher.service
  - no change in boot

drue@xps:~/src/linaro-scratch/work/x15/rootfs/etc/systemd/network$ cat eth.network
[DHCP]
CriticalConnection=true
  - no change in boot

https://gist.github.com/kylemanna/27711c1fcd97d884c072a344046505ba
  - no change in boot

--- re-extracted rootfs to rootfs/ ---

https://gist.github.com/kylemanna/27711c1fcd97d884c072a344046505ba
  - different behavior. It didn't output the dmesg ethernet stuff, but
    it still stalled after:
    [  OK  ] Reached target Multi-User System.
             Starting Update UTMP about System Runlevel Changes...
             Starting Authorization Manager...
    [  OK  ] Started Update UTMP about System Runlevel Changes.
    [  207.955868] nfs: server 10.100.0.60 not responding, still trying


drue@xps:~/src/linaro-scratch/work/x15/rootfs/etc/systemd/network$ cat eth.network
[DHCP]
CriticalConnection=true
  - same as previous... still missing something

# Trying generic qemu rootfs
url: http://people.linaro.org/~daniel.diaz/lkft-qemu/arm32/rpb-console-image-lkft-qemuarm-20190523202859.rootfs.tar.xz

same problem, 
[[0;32m  OK  [0m] Started Serial Getty on ttyS2.
[[0;32m  OK  [0m] Started Network Manager Script Dispatcher Service.
[[0;32m  OK  [0m] Started DNS forwarder and DHCP server.

and then

[  205.133812] nfs: server 10.100.0.60 not responding, still trying
[  205.137404] nfs: server 10.100.0.60 not responding, still trying

## debugging 
drue@xps:~/src/linaro-scratch/work/x15/arm64$ (cd qemu && sudo tar cvzf ../rootfs.tgz .) && scp rootfs.tgz people.linaro.org:~/public_html/files/ && lavacli jobs submit --url juno.yaml

# Modifying following files:
arm64/qemu/etc/systemd/system.conf
arm64/qemu/sbin/dhclient-systemd-wrapper

# Manual x15 munging:

## reboot
drue@lava1:~/lava.therub.org$ docker-compose exec dispatcher /opt/mrv-pdu/MRV-LX5210/mrv.py 10.100.0.40 2 reboot && docker-compose exec dispatcher curl -s http://admin:12345678@10.100.0.41/relay_en.cgi?pulse1=pulse -o /dev/null

## uboot
setenv autoload no
setenv initrd_high 0xffffffff
setenv fdt_high 0xffffffff
dhcp
setenv serverip 10.100.0.60
tftp 0x82000000 drue/tftp-deploy-zx65ju1t/kernel/zImage--5.0+git0+37624b5854-r0-am57xx-evm-20190429002245-1753.bin
setenv initrd_size ${filesize}
tftp 0x88000000 drue/tftp-deploy-zx65ju1t/dtb/zImage--5.0+git0+37624b5854-r0-am57xx-beagle-x15-20190429002245-1753.dtb
setenv bootargs 'console=ttyS2,115200n8 root=/dev/nfs rw nfsroot=10.100.0.60:/var/lib/lava/dispatcher/tmp/drue/extract-nfsrootfs-embywpbk,tcp,hard,intr,vers=3  ip=dhcp'
bootz 0x82000000 - 0x88000000

When booting manually, as above, the qemu root fs works.........
WHY!?


Tried disabling polkit ("Authorization Manager")
drue@xps:~/linaro-scratch/work/x15/arm64/qemu/lib/systemd/system$ diff polkit.service.orig polkit.service
5,8c5,8
< [Service]
< Type=dbus
< BusName=org.freedesktop.PolicyKit1
< ExecStart=/usr/lib/polkit-1/polkitd --no-debug
---
> #[Service]
> #Type=dbus
> #BusName=org.freedesktop.PolicyKit1
> #ExecStart=/usr/lib/polkit-1/polkitd --no-debug

https://lkft.validation.linaro.org/scheduler/job/757536

Didn't even get that far.


