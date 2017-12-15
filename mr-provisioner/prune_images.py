#!/usr/bin/python

# Delete images from mr-provisioner
# Images which:
#   - Belong to me
#   - Are not 'known good'
#   - Are older than a week
#   - Are not attached to a machine
#
# Usage:
#   > PROVISIONER_TOKEN="/BLAHBLAHBLAH=" python3 prune_images.py

import json
import os
import requests
import sys
from datetime import datetime, timedelta
from urllib.parse import urljoin

base_url = "http://172.27.80.1:5000"
token = os.environ.get('PROVISIONER_TOKEN')

def main():

    allowed_types = ["Kernel", "Initrd"]

    headers = {'Authorization': token}

    # Retrieve my own images
    url = urljoin(base_url, "/api/v1/image")

    r = requests.get(url, headers=headers)
    assert r.status_code == 200, 'Error fetching {}, HTTP {} {}'.format(url,
                         r.status_code, r.reason)

    for image in r.json():
        time_of_upload = datetime.strptime(image['upload_date'], "%a, %d %b %Y %H:%M:%S %Z")

        # Delete images that are not "known_good" and are older than 7 days.
        if ((image['known_good'] == False) and
                (datetime.now() - time_of_upload) > timedelta(days=7)):
            print("Deleting {}".format(image))
            url = urljoin(base_url, "/api/v1/image/{}".format(image['id']))
            r = requests.delete(url, headers=headers)
            if r.status_code != 204:
                # These can fail with a 409 if they are in use by a machine
                print('Error deleting {}, HTTP {} {}'.format(url,
                         r.status_code, r.reason))


if __name__ == '__main__':
    main()
