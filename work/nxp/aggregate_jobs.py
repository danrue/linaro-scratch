#!/usr/bin/python3

import fileinput
import json
import subprocess
from pprint import pprint

pass_count = 0
fail_count = 0
fail_by_type = {
    'dns': 0
}
error_msgs = []

for line in fileinput.input():
    job_id = int(line)

    job_status = (
        subprocess.check_output(
            "lavacli -i nxp jobs show {} | grep ^state | awk '{{print $3}}'".format(
                job_id
            ),
            shell=True,
        )
        .strip()
        .decode("utf-8")
    )
    if job_status != "Finished":
        print("jobs {} not finished".format(job_id))
        continue

    # XXX Once https://git.lavasoftware.org/lava/lavacli/issues/15 is fixed, we can
    # skip the grep/awk stuff and do the following instead.
    # job_status = json.loads(subprocess.check_output("lavacli -i nxp jobs show --json {}".format(job_id), shell=True))
    # if job_status.get('state', None) != 'Finished':
    #    print("jobs {} not finished".format(job_id))
    #    continue

    job_results = json.loads(
        subprocess.check_output(
            "lavacli -i nxp results --json {}".format(job_id), shell=True
        )
    )
    job_data = job_results[0]
    result = job_data.get('result') # will be 'fail' or 'pass'
    if result == 'pass':
        pass_count += 1
        continue

    # classify failure
    fail_count += 1
    error_msg = job_data.get('metadata').get('error_msg')
    error_msgs.append(error_msg)
    if 'Name or service not known' in error_msg:
        fail_by_type['dns'] += 1
    else:
        print("warning: uncategorized error_msg: {}".format(error_msg))

print("pass rate: {}%".format(100*pass_count/(pass_count+fail_count)))
print("pass: {}, fail: {}".format(pass_count, fail_count))
pprint(fail_by_type)
pprint(error_msgs)
