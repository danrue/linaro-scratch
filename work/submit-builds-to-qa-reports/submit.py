import json
import os
import requests

url = "https://staging-qa-reports.linaro.org/api/submit/lkft/linux-stable-rc-5.5-oe/v5.5/i386"

metadata = {
    "job_id": "1xxxy",
    "git branch": "linux-5.5.y",
    "git repo": "https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git",
    "git commit": "d5226fa6dbae0569ee43ecfc08bdcd6770fc4755",
    "git describe": "v5.5",
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
    files={
        "tests": json.dumps(tests_file),
        "metadata": json.dumps(metadata),
        "log": json.dumps(log),
    },
)

if not result.ok:
    print(f"Error submitting to qa-reports: {result.reason}: {result.text}")
