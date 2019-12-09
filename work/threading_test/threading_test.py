"""
Experiment with the behavior of many polling threads and the requests library.
"""
import random
import requests
import time
import concurrent.futures

delay_status_update = 30

def get_requests(url, attempts, random_sleep):
    for i in range(attempts):
        if random_sleep:
            time.sleep(random.randrange(delay_status_update))
        else:
            time.sleep(delay_status_update)
        try:
            print(i, end='', flush=True)
            response = requests.get(url)
        except Exception as e:
            print(e)

if __name__ == '__main__':
    url = "https://gist.githubusercontent.com/danrue/f861e22e5697549ac10a574de0983d98/raw/712c7f6fbcd7b0a6fd1d37527436979e678fb8e4/gistfile1.txt"
    with concurrent.futures.ThreadPoolExecutor(max_workers=500) as executor:
        for i in range(500):
            executor.submit(get_requests, url, 10, random_sleep=True)
