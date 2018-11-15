#!/usr/bin/python3

import os
import pdb
import requests

# Snapshot base url without arguments
base_snapshot_url = "http://snapshots.linaro.org"

# base url path e.g. http://snapshots.linaro.org/openembedded/lkft/rocko
base_snapshot_path = "openembedded/lkft/rocko/"

# snapshots branches we care about, e.g.
# http://snapshots.linaro.org/openembedded/lkft/rocko/am57xx-evm/rpb/
snapshot_branches = [
    "linux-next",
    "linux-mainline",
    "linux-stable-rc-4.4",
    "linux-stable-rc-4.9",
    "linux-stable-rc-4.14",
    "linux-stable-rc-4.19",
]

# Map board names (as seen on snapshots) to architectures (as get passed as
# ARCH during linux make)
board_config_map = {
    "juno": "arch/arm64/configs/defconfig",
    "am57xx-evm": "arch/arm/configs/multi_v7_defconfig",
    "intel-core2-32": "arch/x86/configs/i386_defconfig",
    "hikey": "arch/arm64/configs/defconfig",
    "intel-corei7-64": "arch/x86/configs/x86_64_defconfig",
    "dragonboard-410c": "arch/arm64/configs/defconfig",
}

# Map branch names (as used in snapshot_branches) with git repos.
# The second argument is a required url argument, if necessary.
branch_repo_url_map = {
    "linux-next":
        ("https://git.kernel.org/pub/scm/linux/kernel/git/next/linux-next.git/plain/", None),
    "linux-mainline":
        ("https://git.kernel.org/pub/scm/linux/kernel/git/stable/linux.git/plain/", None),
    "linux-stable-rc-4.4":
        ("https://git.kernel.org/pub/scm/linux/kernel/git/stable/linux.git/plain/", "?h=linux-4.4.y"),
    "linux-stable-rc-4.9":
        ("https://git.kernel.org/pub/scm/linux/kernel/git/stable/linux.git/plain/", "?h=linux-4.9.y"),
    "linux-stable-rc-4.14":
        ("https://git.kernel.org/pub/scm/linux/kernel/git/stable/linux.git/plain/", "?h=linux-4.14.y"),
    "linux-stable-rc-4.19":
        ("https://git.kernel.org/pub/scm/linux/kernel/git/stable/linux.git/plain/", "?h=linux-4.19.y"),
}

def get_request(*args):
    r = requests.get(*args)
    r.raise_for_status()
    return r

def urljoiner(*args):
    """
    Joins given arguments into an url. Trailing but not leading slashes are
    stripped for each argument.
    """
    return "/".join(map(lambda x: str(x).rstrip('/'), args))

# Convert None to ""
def xstr(s):
    return s or ""

def save_file(source_url, destination_dir, filename):
    if not os.path.isdir(destination_dir):
        os.makedirs(destination_dir)
    file_path = os.path.join(destination_dir, filename)
    if not os.path.exists(file_path):
        print("Fetching {}...".format(file_path))
        r = get_request(source_url)
        with open(file_path, 'wb') as f:
            f.write(r.content)

def fetch_current_configs():
    url = urljoiner(base_snapshot_url, 'api/ls', base_snapshot_path)
    r = get_request(url)
    for board in r.json()['files']:
        if board['name'] not in board_config_map:
            print("Skipping for {}".format(board['name']))
            continue
        r2 = get_request(urljoiner(base_snapshot_url, 'api/ls', board['url']+'rpb/'))
        for branch in r2.json()['files']:
            if branch['name'] not in snapshot_branches:
                continue

            # Retrieve defconfig from snapshot for the board/branch combination
            destination_path = "snapshot_configs/{}/{}".format(board['name'], branch['name'])
            source_url = urljoiner(base_snapshot_url, branch['url'], "latest", "defconfig")
            save_file(source_url, destination_path, "defconfig")

            # Using same path scheme, retrieve the upstream defconfig
            destination_path = "kernel_configs/{}/{}".format(board['name'], branch['name'])
            source_url = urljoiner(
                branch_repo_url_map[branch['name']][0],
                "{}{}".format(
                    board_config_map[board['name']],
                    xstr(branch_repo_url_map[branch['name']][1])) # branch argument from map structure
            )
            save_file(source_url, destination_path, "defconfig")

def compare_current_configs():
    pass

def main():
    fetch_current_configs()
    compare_current_configs()

if __name__ == '__main__':
    main()
