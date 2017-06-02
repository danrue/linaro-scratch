#!/bin/sh
set -e

RELEASE=centos-erp-1612
TFTP_PATH=${HOME}/tftp/${RELEASE}

mkdir -p ${TFTP_PATH}
if [ ! -f ${TFTP_PATH}/initrd.img ]; then
	wget -o ${TFTP_PATH}/initrd.img http://releases.linaro.org/reference-platform/enterprise/16.12/centos-installer/images/pxeboot/initrd.img
fi
if [ ! -f ${TFTP_PATH}/vmlinuz ]; then
	wget -o ${TFTP_PATH}/vmlinuz http://releases.linaro.org/reference-platform/enterprise/16.12/centos-installer/images/pxeboot/vmlinuz
fi
if [ -f ${HOME}/grub.cfg ]; then
    mv ${HOME}/grub.cfg ${HOME}/.grub.cfg.$(date +%s)
fi
sed s/USERNAME/${USER}/ grub.cfg > ${HOME}/grub.cfg
