#!/bin/bash

plans="plans/rpb_ee/rpb_ee_functional.yaml plans/rpb_ee/rpb_ee_performance.yaml plans/rpb_ee/rpb_ee_stress.yaml"

cd /root/test-definitions
. ./automated/bin/setenv.sh
datetime=$(date +%s)

for plan in ${plans}; do
    plan_short=$(basename -s .yaml ${plan})
    output_path=/root/${plan_short}-${datetime}
    mkdir -p ${output_path}
    test-runner -o ${output_path} -p ${plan} > ${output_path}/stdout.log 2> ${output_path}/stderr.log
    # post-to-squad XXX
done
