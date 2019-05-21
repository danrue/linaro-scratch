bad job:
https://lkft.validation.linaro.org/scheduler/job/735468/definition

bad describe: v4.19.44-106-g6b27ffd29c43
good describe: v4.19.44

http://snapshots.linaro.org/openembedded/lkft/lkft/sumo/intel-corei7-64/lkft/linux-stable-rc-4.19/168

config http://snapshots.linaro.org/openembedded/lkft/lkft/sumo/intel-corei7-64/lkft/linux-stable-rc-4.19/168/config


drue@xps:~/src/linux/4.19-rc$ wget http://snapshots.linaro.org/openembedded/lkft/lkft/sumo/intel-corei7-64/lkft/linux-stable-rc-4.19/168/config
drue@xps:~/src/linux/4.19-rc$ cp config .config
drue@xps:~/src/linux/4.19-rc$ make -j8 bzImage
drue@xps:~/src/linux/4.19-rc$ scp arch/x86/boot/bzImage people.linaro.org:~/public_html/files/4658/bzImage-v4.19.44-79-g5b16be8d41b7
drue@xps:~/src/linux/4.19-rc$ scp arch/x86/boot/bzImage people.linaro.org:~/public_html/files/4658/bzImage-`git describe`




########## BISECTION ###############################################################################
bad  v4.19.44-106-g6b27ffd29c43 https://lkft.validation.linaro.org/scheduler/job/737597
bad  v4.19.44-79-g5b16be8d41b7 https://lkft.validation.linaro.org/scheduler/job/737769
bad  v4.19.44-72-g60d2e47a57ac https://lkft.validation.linaro.org/scheduler/job/737785
???  v4.19.44-71-ge1d4a5e5b7b3 https://lkft.validation.linaro.org/scheduler/job/737791
???  v4.19.44-70-gee71af4a4d3b https://lkft.validation.linaro.org/scheduler/job/737792
bad  v4.19.44-69-g5e621a0d8223 https://lkft.validation.linaro.org/scheduler/job/737790
bad  v4.19.44-68-gb58dc0ea108c https://lkft.validation.linaro.org/scheduler/job/737793
bad  v4.19.44-67-ge8fd3c9a5415 https://lkft.validation.linaro.org/scheduler/job/737794
good v4.19.44-66-ga9e9e87d8955 https://lkft.validation.linaro.org/scheduler/job/737780
good v4.19.44-53-gcde8930c1e7f https://lkft.validation.linaro.org/scheduler/job/737767
good v4.19.44 https://lkft.validation.linaro.org/scheduler/job/737762
####################################################################################################

e8fd3c9a5415f9199e3fc5279e0f1dfcc0a80ab2 is the first bad commit
commit e8fd3c9a5415f9199e3fc5279e0f1dfcc0a80ab2
Author: Theodore Ts'o <tytso@mit.edu>
Date:   Tue Apr 9 23:37:08 2019 -0400

    ext4: protect journal inode's blocks using block_validity
    
    commit 345c0dbf3a30872d9b204db96b5857cd00808cae upstream.
    
    Add the blocks which belong to the journal inode to block_validity's
    system zone so attempts to deallocate or overwrite the journal due a
    corrupted file system where the journal blocks are also claimed by
    another inode.
    
    Bugzilla: https://bugzilla.kernel.org/show_bug.cgi?id=202879
    Signed-off-by: Theodore Ts'o <tytso@mit.edu>
    Cc: stable@kernel.org
    Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

:040000 040000 b8b6ce2577d60c65021e5cc1c3a38b32e0cbb2ff 747c67b159b33e4e1da414b1d33567a5da9ae125 M      fs

### Revert offending commit and see if issue is fixed
drue@xps:~/src/linux/4.19-rc$ git revert 18b3c1c2827c30b5c006d435d3d581cda63142d8 e8fd3c9a5415f9199e3fc5279e0f1dfcc0a80ab2
drue@xps:~/src/linux/4.19-rc$ git describe
v4.19.44-108-g57aff8413acd
https://lkft.validation.linaro.org/scheduler/job/738028
PASS

### Revert offending commit on mainline and see if issue is fixed
drue@xps:~/src/linux/mainline$ git revert fbbbbd2f28aec991f3fbc248df211550fbdfd58c 345c0dbf3a30872d9b204db96b5857cd00808cae
drue@xps:~/src/linux/mainline$ wget http://snapshots.linaro.org/openembedded/lkft/lkft/sumo/intel-corei7-64/lkft/linux-mainline/1828/config
drue@xps:~/src/linux/mainline$ cp config .config
v5.2-rc1-2-g30f948a369a8
drue@xps:~/src/linaro-scratch/bugs/4658$ lavacli jobs submit --url test-mainline.yaml 
https://lkft.validation.linaro.org/scheduler/job/738031
- failed to boot
https://lkft.validation.linaro.org/scheduler/job/738033



http://people.linaro.org/~naresh.kamboju/syscalls





Verify old rootfs with new kernel still fails (it's not a rootfs issue)
drue@xps:~/src/linaro-scratch/bugs/4658$ lavacli jobs submit --url old-rootfs.yaml
https://lkft.validation.linaro.org/scheduler/job/737770
confirmed bad.





drue@xps:~/src/linaro-scratch/bugs/4658$ scp -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no drue root@10.66.17.104:/opt/ltp/runtest/
/opt/ltp/runltp -d /scratch -f drue



echo 'fork13' >> skip
echo 'msgstress01' >> skip
echo 'msgstress02' >> skip
echo 'msgstress03' >> skip
echo 'msgstress04' >> skip
/opt/ltp/runltp -d /scratch -f syscalls -S skip


root@intel-corei7-64:/opt/ltp# while true; do /opt/ltp/runltp -d /scratch -f syscalls -s poll0; mount | grep scr | grep -q rw || break; done

Issue happens in poll02
