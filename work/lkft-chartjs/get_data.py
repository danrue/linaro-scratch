#!/usr/bin/python3 -u

import json
import os
import os.path
import requests
import requests_cache
import sys
import time

requests_cache.install_cache("lkft-reporting")

branches = {"mainline": {"group": "lkft", "slug": "linux-mainline-oe"}}


def urljoiner(*args):
    """
    Joins given arguments into an url. Trailing but not leading slashes are
    stripped for each argument.
    """
    return "/".join(map(lambda x: str(x).rstrip("/"), args))


class qareports:
    def __init__(self, group_slug, project_slug, url="https://qa-reports.linaro.org"):
        self.api_endpoint = urljoiner(url, "api")
        self.group = self._get_group(group_slug)
        self.project = self._get_project(project_slug)


    def _get_group(self, group_slug):
        """ Given a group slug, retrieve the group object """
        url = urljoiner(self.api_endpoint, "groups/?slug={}".format(group_slug))
        result = list(self.get_objects(url))
        if len(result) < 1:
            sys.exit("Error: no group named {} found at {}".format(group_slug, url))
        if len(result) > 1:
            sys.exit("Error: More than one group name matched {} at {}".format(group_slug, url))
        return result[0]

    def _get_project(self, project_slug):
        """ Given a project slug, retrieve the project object """
        url = urljoiner(self.api_endpoint, "projects/?slug={}&group={}".format(project_slug, self.group['id']))
        result = list(self.get_objects(url))
        if len(result) < 1:
            sys.exit("Error: no project named {} found at {}".format(project_slug, url))
        if len(result) > 1:
            sys.exit("Error: More than one project name matched {} at {}".format(project_slug, url))
        return result[0]


    def get_url(self, url, retries=3):
        print(url)
        r = requests.get(url)
        try:
            r.raise_for_status()
        except:
            if retries <= 0:
                raise
            print("Retrying {}".format(url))
            time.sleep(30)
            return self.get_url(url, retries=retries - 1)
        return r

    def get_object(self, url, cache=True):
        """
        Retrieve a url.
        """

        result = self.get_url(url).json()

        return result

    def get_objects(self, url):
        """
        Retrieve all objects

        Expects a url with 'count', 'next', 'results' fields.
        """
        r = self.get_url(url)
        for obj in r.json()["results"]:
            yield self.get_object(obj["url"])
        if r.json()["next"] is not None:
            yield from self.get_objects(r.json()["next"])

    @property
    def builds(self):
        ''' Return a build generator '''
        return self.get_objects(urljoiner(self.api_endpoint, "projects", self.project['id'], 'builds'))

    def status(self, build_id):
        """ Given a build ID, return a status object """
        return self.get_object(urljoiner(self.api_endpoint, "builds", build_id, 'status'))

    def get_leaf_objects(self, url):
        """
        Retrieve objects which are paged and collapse into a single list.
        """

        result = self.read_from_cache(url)
        if result is not None:
            return result

        results = []
        r = self.get_url(url)
        for obj in r.json()["results"]:
            results.append(obj)
        while r.json()["next"] is not None:
            r = self.get_url(r.json()["next"])
            for obj in r.json()["results"]:
                results.append(obj)

        self.save_to_cache(url, results)
        return results


if __name__ == "__main__":
    for branch_name, branch_values in branches.items():
        client = qareports(branch_values['group'], branch_values['slug'])
        for build in client.builds:
            status = client.status(build['id'])
            total_tests = status['tests_pass']+status['tests_fail']+status['tests_xfail']
            print(total_tests)

