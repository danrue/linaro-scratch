#!/usr/bin/python3

import os
import pdb
import requests
import subprocess

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
board_arch_map = {
    "juno": "arm64",
    "am57xx-evm": "arm",
    "intel-core2-32": "i386",
    "hikey": "arm64",
    "intel-corei7-64": "x86_64",
    "dragonboard-410c": "arm64",
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

            # Retrieve config from snapshot for the board/branch combination
            destination_path = "snapshot_configs/{}/{}".format(board['name'], branch['name'])
            source_url = urljoiner(base_snapshot_url, branch['url'], "latest", "config")
            save_file(source_url, destination_path, "config")

            # Using same path scheme, retrieve the upstream defconfig
            destination_path = "kernel_configs/{}/{}".format(board['name'], branch['name'])
            source_url = urljoiner(
                branch_repo_url_map[branch['name']][0],
                "{}{}".format(
                    board_config_map[board['name']],
                    xstr(branch_repo_url_map[branch['name']][1])) # branch argument from map structure
            )
            save_file(source_url, destination_path, "defconfig")

def run(command):
    print(command)
    subprocess.run(command, check=True, shell=True)


branch_board_build_map = {
    "mainline": {
        "build_number": "1411",  # v4.20-rc4
        "version": "v4.20-rc4",
        "boards": [
            "am57xx-evm",
            "dragonboard-410c",
            "hikey",
            "intel-core2-32",
            "intel-corei7-64",
            "juno",
        ],
        "label": "docker-stretch-amd64",
        "base_url": "https://ci.linaro.org/job/openembedded-lkft-linux-mainline/DISTRO=rpb,MACHINE=",
    },
    "4.19": {
        "build_number": "27",  # v4.19.5
        "version": "v4.19.5",
        "boards": [
            "am57xx-evm",
            "dragonboard-410c",
            "hikey",
            "intel-core2-32",
            "intel-corei7-64",
            "juno",
        ],
        "label": "docker-lkft",
        "base_url": "https://ci.linaro.org/job/openembedded-lkft-linux-stable-rc-4.19/DISTRO=rpb,MACHINE=",
    },
    "4.14": {
        "build_number": "338",  # v4.14.84
        "version": "v4.14.84",
        "boards": [
            "am57xx-evm",
            "dragonboard-410c",
            "hikey",
            "intel-core2-32",
            "intel-corei7-64",
            "juno",
        ],
        "label": "docker-lkft",
        "base_url": "https://ci.linaro.org/job/openembedded-lkft-linux-stable-rc-4.14/DISTRO=rpb,MACHINE=",
    },
    "4.9": {
        "build_number": "430",  # v4.9.141
        "version": "v4.9.141",
        "boards": [
            "am57xx-evm",
            "dragonboard-410c",
            "hikey",
            "intel-core2-32",
            "intel-corei7-64",
            "juno",
        ],
        "label": "docker-lkft",
        "base_url": "https://ci.linaro.org/job/openembedded-lkft-linux-stable-rc-4.9/DISTRO=rpb,MACHINE=",
    },
    "4.4": {
        "build_number": "358",  # v4.4.165
        "version": "v4.4.165",
        "boards": [
            "am57xx-evm",
            "intel-core2-32",
            "intel-corei7-64",
            "juno",
        ],
        "label": "docker-lkft",
        "base_url": "https://ci.linaro.org/job/openembedded-lkft-linux-stable-rc-4.4/DISTRO=rpb,MACHINE=",
    },
    "4.4-hikey": {
        "build_number": "262",  # v4.4.165-rc2
        #"version": "v4.4.165-rc2",
        "version": "4.4.165-rc2-hikey-20181126-324",
        "boards": [
            "hikey",
        ],
        "label": "docker-stretch-amd64",
        "base_url": "https://ci.linaro.org/job/openembedded-lkft-linaro-hikey-stable-rc-4.4/DISTRO=rpb,MACHINE=",
    },
}

def build_oe_configs():
    run("mkdir -p loeb")
    os.chdir("loeb")
    HOME = os.environ.get("HOME")
    run("mkdir -p {}/oe-downloads".format(HOME))
    run("mkdir -p {}/oe-sstate-cache".format(HOME))
    run("ln -sf {}/oe-downloads downloads".format(HOME))
    run("ln -sf {}/oe-sstate-cache sstate-cache".format(HOME))
    run("rm -f .loeb.config")
    run("loeb copyconfig https://ci.linaro.org/job/openembedded-lkft-linux-mainline/1418/DISTRO=rpb,MACHINE=intel-corei7-64,label=docker-stretch-amd64/")
    run("loeb init --quiet")

    for branch_name, branch in branch_board_build_map.items():
        for board in branch['boards']:
            build_dir = "build-{}".format(branch_name)
            os.putenv("BUILD_DIR", build_dir)
            run("loeb reset -f")
            build_url = branch['base_url'] + board + ',label=' + branch['label'] + '/' + branch['build_number'] + '/'
            run("rm -f .loeb.config")
            run("loeb copyconfig {}".format(build_url))
            run("loeb apply lkft")
            run("sed -i 's%96boards/meta-96boards\"%danrue/meta-96boards\" revision=\"rocko-no-kselftest\"%g' .repo/manifest.xml")
            run('repo sync --force-sync')
            run("loeb env bitbake -c configure virtual/kernel") # cp -p tmp-rpb-glibc/work/*/linux-generic*/*/*/defconfig unique_defconfig
            #run("loeb env bitbake rpb-console-image")
            run('mkdir -p ../lkft-configs/{}'.format(branch['version']))
            #run('cp {}/tmp*/deploy/images/*/defconfig ../lkft-configs/{}/{}.defconfig'.format(build_dir, branch['version'], board))
            run('cp {}/tmp-rpb-glibc/work/*/linux-generic*/*/*/defconfig ../lkft-configs/{}/{}.defconfig'.format(build_dir, branch['version'], board))
            #import pdb; pdb.set_trace()


def build_linux_configs():
    # Assume linux/<branch> exists and is up to date
    for branch_name, branch in branch_board_build_map.items():
        for arch in ['x86_64', 'i386', 'arm64', 'arm']:
            os.chdir('linux/{}'.format(branch_name))
            run('git reset --hard {}'.format(branch['version']))
            run('make ARCH={} defconfig'.format(arch))
            run('make savedefconfig')
            run('mkdir -p ../../linux-configs/{}'.format(branch['version']))
            run('cp defconfig ../../linux-configs/{}/{}.defconfig'.format(branch['version'], arch))
            os.chdir('../../')

def compare_configs():
    for branch_name, branch in branch_board_build_map.items():
        for board in branch['boards']:
            run('mkdir -p lkft-fragments/{}'.format(branch['version']))
            run('diffconfig -m linux-configs/{}/{}.defconfig lkft-configs/{}/{}.defconfig > lkft-fragments/{}/{}.frag'.format(
                branch['version'], board_arch_map[board], branch['version'], board, branch['version'], board))


def main():
    #fetch_current_configs() # This turned out not to be useful, because production
                             # built defconfigs contain kselftest configs merged in

    #build_oe_configs()
    #build_linux_configs()
    compare_configs()

if __name__ == '__main__':
    main()
