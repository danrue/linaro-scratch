#!/bin/bash
set -e
set -x

apt update
apt install -y tmux git python-pip
tmux new -s erp
git clone https://git.linaro.org/people/dan.rue/qa/test-definitions.git
cd test-definitions
. automated/bin/setenv.sh
pip install -r automated/utils/requirements.txt
test-runner -p plans/rpb_ee/rpb_ee_enterprise.yaml
