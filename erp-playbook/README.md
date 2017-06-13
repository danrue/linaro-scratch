ERP Test Harness
================

This ansible playbook can be used to automate the ERP testing on a set of given
hosts.

Usage
-----

Add hosts to `hosts` file. Run `make`.

Ansible will ssh into each host in hosts, install test-definitions
prerequisites, clone test-definitions, run each test plan that is used for ERP
testing, and post the results to https://qa-reports.linaro.org/.

The ansible run is idempotent; each time it is run, if the tests are already
running on a host it will not do anything. If the tests are not running on a
host, it will start them.
