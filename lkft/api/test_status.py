import requests
import sys
import tabulate

projects = [
    "linux-mainline-oe",
    "linux-next-oe",
    "linux-stable-4.14-oe",
    "linux-stable-rc-4.14-oe",
    "linux-stable-4.9-oe",
    "linux-stable-rc-4.9-oe",
    "linux-stable-4.4-oe",
    "linux-stable-rc-4.4-oe",
    "linux-hikey-stable-4.4-oe",
    "linux-hikey-stable-rc-4.4-oe",
]

base_url = "https://qa-reports.linaro.org/api/"

def find_test_results(needle):
    ''' Given a test name, find test results across branches '''

    for project in projects:
        project_url = "{}projects/?slug={}".format(base_url, project)
        project_results = requests.get(project_url).json()
        assert project_results['count'] == 1
        latest_build = requests.get(project_results['results'][0]['builds']).json()['results'][0]

        testruns = requests.get(latest_build['testruns']).json()['results']

        for testrun in testruns:

            # XXX This is really expensive.
            # It would be better if we could look in testjobs, filter by name, and then
            # look at the specific testrun that we care about. As-written, we have
            # to look at all testruns.
            tests = requests.get(testrun['tests']).json()['results']
            for test in tests:
                if needle in test['name']:
                    environment = requests.get(testrun['environment']).json()
                    print("{} {} {} {}".format(
                            project,
                            environment['name'],
                            test['name'],
                            test['result']
                         ))

if __name__ == "__main__":
    find_test_results('bitmap.sh')
