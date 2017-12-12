import requests
import sys

def get_all_results(url, results=[]):
    data = requests.get(url).json()
    if data['next']:
        return get_all_results(data['next'], results)
    else:
        return results+data['results']

def is_build_complete(list_of_testjobs):
    if len(list_of_testjobs) < 1:
        return False
    for testrun in testjobs:
        if not testrun['fetched']:
            return False
    return True

project_slug = "linux-mainline-oe"
builds_to_check = 10
base_url = "https://qa-reports.linaro.org/api/"

project_url = "{}projects/?slug={}".format(base_url, project_slug)
projects = requests.get(project_url).json()
assert projects['count'] == 1
builds = requests.get(projects['results'][0]['builds']).json()

for i in range(builds_to_check):
    testjobs = get_all_results(builds['results'][i]['testjobs'])
    if not is_build_complete(testjobs):
        sys.exit("Error, build {} in project {} has not yet completed".
                 format(builds['results'][i]['version'], project_slug))

