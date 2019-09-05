#!/bin/sh

# Reproduce kselftest jobs from https://qa-reports.linaro.org/lkft/linux-stable-rc-4.9-oe/build/v4.9.190/#!?details=139
# except using in kernel version of kselftest. Compare results

jobs="https://lkft.validation.linaro.org/scheduler/job/897620/definition/plain https://lkft.validation.linaro.org/scheduler/job/897289/definition/plain https://lkft.validation.linaro.org/scheduler/job/897661/definition/plain https://lkft.validation.linaro.org/scheduler/job/897324/definition/plain https://lkft.validation.linaro.org/scheduler/job/897481/definition/plain https://lkft.validation.linaro.org/scheduler/job/897601/definition/plain https://lkft.validation.linaro.org/scheduler/job/897463/definition/plain https://lkft.validation.linaro.org/scheduler/job/897621/definition/plain https://lkft.validation.linaro.org/scheduler/job/897288/definition/plain https://lkft.validation.linaro.org/scheduler/job/897443/definition/plain"

for job in $jobs; do
    curl -s $job | sed 's/mainline/default-in-kernel/' | lavacli jobs submit --url -
done

