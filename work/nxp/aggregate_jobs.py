#!/usr/bin/python3
#
# Copyright 2019, Linaro Limited
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
# of the Software, and to permit persons to whom the Software is furnished to do
# so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import fileinput
import json
import statistics
import subprocess
from dateutil import parser
from pprint import pprint

pass_count = 0
fail_count = 0
failure_strings = [
    "Name or service not known",
    "bootloader-interrupt timed out",
]
fail_by_type = {}
for failure_string in failure_strings:
    fail_by_type[failure_string] = 0
error_msgs = []
durations = []  # list of successful job durations in seconds

for line in fileinput.input():
    job_id = int(line)

    print("job {}: fetching".format(job_id))
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
        print("jobs {}: not finished".format(job_id))
        continue

    # XXX Once https://git.lavasoftware.org/lava/lavacli/issues/15 is fixed, we can
    # skip the grep/awk stuff above and just use the following instead.
    # In the meantime, this is slightly inefficient.
    job_status = json.loads(
        subprocess.check_output(
            "lavacli -i nxp jobs show --json {}".format(job_id), shell=True
        )
    )
    if job_status.get("state", None) != "Finished":
        print("jobs {} not finished".format(job_id))
        continue

    job_results = json.loads(
        subprocess.check_output(
            "lavacli -i nxp results --json {}".format(job_id), shell=True
        )
    )
    job_data = job_results[0]
    result = job_data.get("result")  # will be 'fail' or 'pass'
    if result == "pass":
        pass_count += 1
        durations.append(
            (
                parser.parse(job_status.get("end_time"))
                - parser.parse(job_status.get("start_time"))
            ).seconds
        )
        continue

    # classify failure
    fail_count += 1
    error_msg = job_data.get("metadata").get("error_msg")
    error_msgs.append(error_msg)
    for failure_string in failure_strings:
        if failure_string in error_msg:
            fail_by_type[failure_string] += 1
            print("job {}: failure detected: {}".format(job_id, failure_string))
            break
    else:
        print("job {}: warning: uncategorized error_msg: {}".format(job_id, error_msg))

print("pass rate: {:.2f}%".format(100 * pass_count / (pass_count + fail_count)))
print("pass: {}, fail: {}".format(pass_count, fail_count))
for fail_type, count in fail_by_type.items():
    if count > 0:
        print(
            "{:.2f}% of jobs failed for reason: {}".format(
                100 * count / (pass_count + fail_count), fail_type
            )
        )
print("durations of successful jobs:")
print("    min: {}s".format(min(durations)))
print("    max: {}s".format(max(durations)))
print("    mean: {}s".format(int(statistics.mean(durations))))
print("    median: {}s".format(int(statistics.median(durations))))
print("    standard deviation: {}s".format(int(statistics.stdev(durations))))
