#!/bin/sh
set -e

RELEASE=debian-erp-1612
TFTP_PATH=${HOME}/tftp/${RELEASE}

mkdir -p ${TFTP_PATH}
if [ ! -f ${TFTP_PATH}/initrd.gz ]; then
	wget -o ${TFTP_PATH}/initrd.gz http://releases.linaro.org/reference-platform/enterprise/16.12/debian-installer/debian-installer/arm64/initrd.gz
fi
if [ ! -f ${TFTP_PATH}/linux ]; then
	wget -o ${TFTP_PATH}/linux http://releases.linaro.org/reference-platform/enterprise/16.12/debian-installer/debian-installer/arm64/linux
fi
if [ -f ${HOME}/grub.cfg ]; then
    mv ${HOME}/grub.cfg ${HOME}/.grub.cfg.$(date +%s)
fi
sed s/USERNAME/${USER}/ grub.cfg > ${HOME}/grub.cfg
