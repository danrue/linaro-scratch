import json
import requests
import sys

# Given a tuxbuild url, download the information about the build,
# generate a kcidb build report, and submit it.


def get_revisions(status):
    revision = {
        "id": status.get("git_sha"),
        "origin": origin,
        "git_repository_url": status.get("git_repo"),
        "git_commit_hash": status.get("git_sha"),
        "git_commit_name": status.get("git_describe"),
    }
    if status.get("git_ref"):
        revision["git_repository_branch"] = status.get("git_ref")
    return [revision]


def get_builds(status):
    build = {
        "id": f"{origin}:{status.get('build_key')}",
        "revision_id": status.get("git_sha"),
        "origin": origin,
        "architecture": status.get("target_arch"),
        "compiler": status.get("toolchain"),
        "config_name": status.get("kconfig")[0],  # XXX
        "config_url": f"{status.get('download_url')}config",
        "log_url": f"{status.get('download_url')}build.log",
        "valid": status.get("build_status") == "pass",
    }
    return [build]


origin = "tuxsuite"

tuxbuild_url = sys.argv[1].rstrip("/")
request = requests.get(f"{tuxbuild_url}/status.json")
request.raise_for_status()
status = request.json()

payload = {
    "revisions": get_revisions(status),
    "builds": get_builds(status),
    "version": {
        "major": 3,
        "minor": 0,
    },
}

print(json.dumps(payload, sort_keys=True, indent=4))
