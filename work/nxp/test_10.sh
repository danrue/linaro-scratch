JOBS=10
for i in $(seq 1 $JOBS); do lavacli -i nxp jobs submit job_43.yaml | tee -a test_$JOBS.jobs; done
