import json
import os
import requests
import time

url = "https://staging-qa-reports.linaro.org/api/submit/lkft/linux-stable-rc-5.5-oe/v5.5/i386"

metadata = {
    "job_id": f"{time.time()}",
    "make_kernelversion": "5.5.0",
}
log = "make output"
tests_file = {
    "build/build-arm64-gcc-9": "pass",  # or "fail"
}
headers = {
    "Auth-Token": os.environ["QA_TOKEN"],
}

result = requests.post(
    url,
    headers=headers,
    json={"metadata": metadata, "log": log, "tests_file": tests_file},
)

if not result.ok:
    print(f"Error submitting to qa-reports: {result.reason}: {result.text}")


metadata = {
    "job_id": f"{time.time()}",
    "make_kernelversion": "5.5.0",
}
result = requests.post(
    url,
    headers=headers,
    files={
        "tests": json.dumps(tests_file),
        "metadata": json.dumps(metadata),
        "log": json.dumps(log),
    },
)

if not result.ok:
    print(f"Error submitting to qa-reports: {result.reason}: {result.text}")
