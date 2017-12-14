#!/usr/bin/env python3

"""
    Given a pre-defined list of projects and environments and a test name to
    search for, look through the latest build of each project and report the
    results of the given test name

    Example usage:
        python3 test_status.py 'kselftest/bitmap.sh'

    Bugs:
        - Very slow. Has to retrieve each and every testrun for each build.
          - Not sure how to solve this. If testruns was available from testjobs,
            we would still need to know which tests are in which runs.
        - If a build is not complete, it is not smart enough to know (it is also
          expensive to calculate), and as a result may report missing data.
          - Requested in https://projects.linaro.org/browse/QA-1785

"""

import argparse
import requests
import sys
from tabulate import tabulate

projects = [
    "linux-mainline-oe",
    "linux-next-oe",
    "linux-stable-4.14-oe",
    "linux-stable-rc-4.14-oe",
    "linux-stable-4.9-oe",
    "linux-stable-rc-4.9-oe",
    "linux-stable-4.4-oe",
    "linux-stable-rc-4.4-oe",
    "linaro-hikey-stable-4.4-oe",
    "linaro-hikey-stable-rc-4.4-oe",
]

environments = [
    "hi6220-hikey",
    "x86",
    "x15",
    "juno-r2"
]

base_url = "https://qa-reports.linaro.org/api/"

def get(url):
    sys.stdout.write('.')
    sys.stdout.flush()
    return requests.get(url)

def get_all_results(url, results=[]):
    data = get(url).json()
    if data.get('next'):
        return get_all_results(data['next'], results)
    else:
        return results+data['results']

def find_test_results(needle):
    ''' Given a test name, find test results across branches '''

    results = []
    for project in projects:
        project_result = {}
        project_url = "{}projects/?slug={}".format(base_url, project)
        project_results = get(project_url).json()
        assert project_results['count'] == 1, 'project {} not found'.format(project)
        latest_build = get(project_results['results'][0]['builds']).json()['results'][1]

        project_result['project'] = project
        project_result['version'] = latest_build['version']

        testruns = get_all_results(latest_build['testruns'])

        for testrun in testruns:

            # XXX This is really expensive.
            # It would be better if we could look in testjobs, filter by name, and then
            # look at the specific testrun that we care about. As-written, we have
            # to look at all testruns.
            tests = get_all_results(testrun['tests'])
            for test in tests:
                if needle == test['name']:
                    environment = get(testrun['environment']).json()
                    project_result[environment['slug']] = test['result']

        results.append(project_result)
    sys.stdout.write("\n\n")
    return results

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Find test results for a given test.')
    parser.add_argument('test_name', type=str,
                        help='Test name to look for.')
    args = parser.parse_args()

    results = find_test_results(args.test_name)
    print(tabulate(results, headers='keys', tablefmt='presto'))

