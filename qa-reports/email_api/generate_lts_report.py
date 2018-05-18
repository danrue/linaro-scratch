import requests
import sys

def usage():
    print("{} [4.4|4.9|4.14|4.16]".format(sys.argv[0]))
    sys.exit(1)

if len(sys.argv) < 2:
    usage()
branch = sys.argv[1]
if branch not in ['4.4', '4.9', '4.14', '4.16']:
    usage()

projects = {
    'linaro-hikey-stable-rc-4.4-oe': 'https://qa-reports.linaro.org/api/projects/34/',
    'linux-stable-rc-4.4-oe': 'https://qa-reports.linaro.org/api/projects/40/',
    'linux-stable-rc-4.9-oe': 'https://qa-reports.linaro.org/api/projects/23/',
    'linux-stable-rc-4.14-oe': 'https://qa-reports.linaro.org/api/projects/58/',
    'linux-stable-rc-4.16-oe': 'https://qa-reports.linaro.org/api/projects/101/',
}

branches = {
    '4.4': [
        'https://qa-reports.linaro.org/api/projects/34/',
        'https://qa-reports.linaro.org/api/projects/40/',
    ],
    '4.9': ['https://qa-reports.linaro.org/api/projects/23/'],
    '4.14': ['https://qa-reports.linaro.org/api/projects/58/'],
    '4.16': ['https://qa-reports.linaro.org/api/projects/101/'],

}

for url in branches[branch]:
    r = requests.get(url+'builds')
    result = r.json()['results'][0]
    r = requests.get(result['url']+'email?template=9')
    print(r.text)


