#!/usr/bin/env python3
import argparse
import json
import requests

from netrcauth import Auth
from proxy import LAVA
from pprint import pprint

import logging

# These two lines enable debugging at httplib level (requests->urllib3->http.client)
# You will see the REQUEST, including HEADERS and DATA, and RESPONSE with HEADERS but without DATA.
# The only thing missing will be the response.body which is not logged.
try:
    import http.client as http_client
except ImportError:
    # Python 2
    import httplib as http_client
#http_client.HTTPConnection.debuglevel = 1

# You must initialize logging, otherwise you'll not see debug output.
logging.basicConfig()
#logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
#requests_log.propagate = True

def get_objects(endpoint_url, expect_one=False, parameters={}):
    """
    gets list of objects from endpoint_url
    optional parameters allow for filtering
    expect_count
    """
    obj_r = requests.get(endpoint_url, parameters)
    if obj_r.status_code == 200:
        objs = obj_r.json()
        if 'count' in objs.keys():
            if expect_one and objs['count'] == 1:
                return objs['results'][0]
            else:
                ret_obj = []
                while True:
                    for obj in objs['results']:
                        ret_obj.append(obj)
                    if objs['next'] is None:
                        break
                    else:
                        obj_r = requests.get(objs['next'])
                        if obj_r.status_code == 200:
                            objs = obj_r.json()
                return ret_obj
        else:
            return objs

def get_testrun_results(squad_url, build, environment):
    testruns_url = squad_url + "/api/testruns/"
    params = {"environment": environment['id'], "build": build['id']}
    testruns = get_objects(testruns_url, False, params)
    results = {}
    for testrun in testruns:
        _results_resp = requests.get(testrun['tests_file'])
        _results = _results_resp.json()
        results.update(_results)
    return results


def dict_compare(d1, d2):
    d1_keys = set(d1.keys())
    d2_keys = set(d2.keys())
    intersect_keys = d1_keys.intersection(d2_keys)
    added = d1_keys - d2_keys
    removed = d2_keys - d1_keys
    modified = {o : (d1[o], d2[o]) for o in intersect_keys if d1[o] != d2[o]}
    same = set(o for o in intersect_keys if d1[o] == d2[o])
    return added, removed, modified, same


def main():

    parser = argparse.ArgumentParser(description='Compare SQUAD projects')
    parser.add_argument('--source-project-slug',
        dest='source_project_slug',
        required=True,
        help='slug of the base project for the result comparison')
    parser.add_argument('--target-project-slug',
        dest='target_project_slug',
        required=True,
        help='slug of the target project for the result comparison')
    parser.add_argument('--squad-url',
        dest='squad_url',
        required=True,
        help='URL of SQUAD instance in form https://example.com')

    args = parser.parse_args()
    params={"slug": args.source_project_slug}
    base_url = args.squad_url + "/api/projects/"
    builds_url = args.squad_url + "/api/builds/"
    envs_url = args.squad_url + "/api/environments/"

    project = get_objects(base_url, True, params)
    project_envs = get_objects(envs_url, False, {"project": project['id']})
    params = {"slug": args.target_project_slug}
    target_project = get_objects(base_url, True, params)
    target_project_envs = get_objects(envs_url, False, {"project": target_project['id']})
    # can't search in versions through the API yet :(
    # this will be fixed by https://github.com/Linaro/squad/pull/208
    build_list = get_objects(project['builds'])
    for build in build_list:
        # get the corresponding build from target project
        target_build = get_objects(builds_url, True, {"project": target_project['id'], "version": build['version']})
        print("\nProcessing build %s" % build['version'])
        if target_build: 
            for env in target_project_envs:
                source_env = None
                for s_env in project_envs:
                    if s_env['slug'] == env['slug']:
                        source_env = s_env
                        break
                if source_env is not None:
                    print("Data for %s" % env['slug'])
                    source_results = get_testrun_results(args.squad_url, build, source_env)
                    target_results = get_testrun_results(args.squad_url, target_build, env)
                    added, removed, modified, same = dict_compare(source_results, target_results)
                    if added:
                        print("New in %s project" % target_project['name'])
                        pprint(added)

                    if removed:
                        print("Missing in %s project" % target_project['name'])
                        pprint(removed)

                    if modified:
                        print("Different between %s and %s projects" % (target_project['name'], project['name']))
                        pprint(modified)
                else:
                    print("No data for %s" % env['slug'])

if __name__ == "__main__":
    main()
