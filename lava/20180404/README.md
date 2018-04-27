qemu filesystem stability testing
- original qemu: https://lkft.validation.linaro.org/scheduler/job/139366
- libvert https://lkft.validation.linaro.org/scheduler/job/147545
- ~/src/linaro-scratch/lava/20180404$

$ for i in `seq 1 28`; do lavacli jobs submit job_139366.yaml; done
$ for i in `seq 170085 170112`; do lavacli jobs show $i; done | grep ^state
$ for i in `seq 170085 170112 `; do echo $i; lavacli results $i | grep fail; done
