#!/bin/bash

export BUILD_CAUSE=UPSTREAMTRIGGER
export BUILD_CAUSE_UPSTREAMTRIGGER=true
export BUILD_DISPLAY_NAME=#5
export BUILD_ID=5
export BUILD_NAME=4.4
export BUILD_NUMBER=5
export BUILD_TAG=jenkins-lkft-lava-staging-oe-BUILD_NAME=4.4,DEVICE_TYPE=hi6220-hikey-5
export BUILD_URL=https://ci.linaro.org/job/lkft-lava-staging-oe/BUILD_NAME=4.4,DEVICE_TYPE=hi6220-hikey/5/
export CA_CERTIFICATES_JAVA_VERSION=20161107~bpo8+1
export COPY_REFERENCE_FILE_LOG=/var/jenkins_home/copy_reference_file.log
export DEVICE_TYPE=hi6220-hikey
export EXECUTOR_NUMBER=6
export HOME=/var/jenkins_home
export HOSTNAME=154e3e9c9816
export HUDSON_HOME=/var/jenkins_home
export HUDSON_SERVER_COOKIE=bd3c6a001cafdac9
export HUDSON_URL=https://ci.linaro.org/
export JAVA_DEBIAN_VERSION=8u131-b11-1~bpo8+1
export JAVA_HOME=/docker-java-home
export JAVA_VERSION=8u131
export JENKINS_HOME=/var/jenkins_home
export JENKINS_SERVER_COOKIE=bd3c6a001cafdac9
export JENKINS_SLAVE_AGENT_PORT=50000
export JENKINS_UC=https://updates.jenkins.io
export JENKINS_URL=https://ci.linaro.org/
export JENKINS_VERSION=2.46.3
export JOB_BASE_NAME=BUILD_NAME=4.4,DEVICE_TYPE=hi6220-hikey
export BUILD_NAME=4.4
export DEVICE_TYPE=hi6220-hikey
export JOB_URL=https://ci.linaro.org/job/lkft-lava-staging-oe/BUILD_NAME=4.4,DEVICE_TYPE=hi6220-hikey/
export LANG=C.UTF-8
export LAVA_SERVER=https://staging.validation.linaro.org/RPC2/
export NODE_LABELS=flyweight master
export NODE_NAME=master
export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
export PWD=/
export QA_SERVER=https://qa-reports.linaro.org
export ROOT_BUILD_CAUSE=MANUALTRIGGER
export ROOT_BUILD_CAUSE_MANUALTRIGGER=true
export RUN_CHANGES_DISPLAY_URL=https://ci.linaro.org/job/lkft-lava-staging-oe/BUILD_NAME=4.4,DEVICE_TYPE=hi6220-hikey/5/display/redirect?page=changes
export RUN_DISPLAY_URL=https://ci.linaro.org/job/lkft-lava-staging-oe/BUILD_NAME=4.4,DEVICE_TYPE=hi6220-hikey/5/display/redirect
export SHLVL=0
export TINI_SHA=6c41ec7d33e857d4779f14d9c74924cab0c7973485d2972419a3b7c7620ff5fd
export TINI_VERSION=0.14.0

export SNAPSHOTS_BASE_URL="https://snapshots.linaro.org/openembedded/lkft/morty/hikey/rpb/${BUILD_NAME}/latest/"

MD5_FILENAME="MD5SUMS.txt"
wget -O "${MD5_FILENAME}" "${SNAPSHOTS_BASE_URL}${MD5_FILENAME}"
ROOTFS_FILENAME=$(grep -E "rpb-console-image-hikey-[0-9]{14}-[0-9]{2}\.rootfs\.img\.gz" "${MD5_FILENAME}" | awk '{print $2}')
BOOT_FILENAME=$(grep -E "boot\S*uefi\.img" "${MD5_FILENAME}" | awk '{print $2}')


#export QA_SERVER="http://localhost:8000"
export QA_REPORTS_TOKEN=""
export DEVICE_TYPE="hi6220-hikey"
export KERNEL_DESCRIBE="kernel describe"
export KSELFTEST_SKIPLIST="pstore"
export BOOT_URL="${SNAPSHOTS_BASE_URL}${BOOT_FILENAME}"
export SYSTEM_URL="${SNAPSHOTS_BASE_URL}${ROOTFS_FILENAME}"
export KERNEL_BRANCH=${BUILD_NAME}
export KERNEL_VERSION=${BUILD_NAME}
export KERNEL_REPO="https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/"
export KERNEL_COMMIT=${BUILD_NUMBER}
export KERNEL_DESCRIBE="Kernel Describe"

python configs/openembedded-lkft/submit_for_testing.py \
    --device-type ${DEVICE_TYPE} \
    --build-number ${BUILD_NUMBER} \
    --lava-server ${LAVA_SERVER} \
    --qa-server ${QA_SERVER} \
    --qa-server-team staging-lkft \
    --qa-server-project ${BUILD_NAME} \
    --git-commit ${BUILD_NUMBER} \
    --template-names template-kselftest.yaml
#    --template-names template-kselftest.yaml template-ltp.yaml template-libhugetlbfs.yaml


