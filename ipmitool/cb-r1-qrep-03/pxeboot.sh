BMC=172.27.64.153
BMCU=admin
BMCP=admin
ipmitool -v -I lanplus -H ${BMC} -U ${BMCU} -P ${BMCP} chassis bootdev pxe
ipmitool -v -I lanplus -H ${BMC} -U ${BMCU} -P ${BMCP} chassis power reset
