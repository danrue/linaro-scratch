Debugging x15

# extract rootfs
mkdir rootfs; cd rootfs; sudo tar xf ../rpb...

# modify rootfs as needed
# repackage rootfs and submit lava job
drue@xps:~/src/linaro-scratch/work/x15$ (cd rootfs && sudo tar cvzf ../rootfs.tgz .) && scp rootfs.tgz people.linaro.org:~/public_html/files/ && lavacli -i ther
ub jobs submit --url x15_uboot.yaml

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

