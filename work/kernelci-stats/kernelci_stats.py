import os
import re

import plotly.plotly as py
import plotly.graph_objs as go
from email.utils import parsedate_to_datetime
from email.parser import BytesParser, Parser
from email.policy import default

lists_stable = "/home/drue/.mail/linaro/lists-stable"
stable_review_re = re.compile('^\[PATCH \d+\.\d+ \d+/(\d+)\] (\d+\.\d+\.\d+)-stable review$')
kernelci_stable_rc_re = re.compile('^stable-rc/linux-\d+\.\d+\.y build: \d+ builds: \d+ failed, \d+ passed, \d+ errors, \d+ warnings \((v\d+\.\d+\.\d+-\d+-g\w+)\)$')

class mail_message():
    def __init__(self, contents):
        self.contents = contents.decode(errors='ignore')

    @property
    def is_stable_review(self):
        """ Determine whether or not mail is a stable-rc review email """
        # Subject: [PATCH 5.0 000/122] 5.0.14-stable review
        headers = Parser(policy=default).parsestr(self.contents)
        self.subject = headers['subject']

        try:
            m = stable_review_re.match(self.subject)
        except:
            return False
        if not m:
            return False

        self.stable_patch_count = int(m.group(1))
        self.stable_rc_version = m.group(2)

        self.mail_date = parsedate_to_datetime(headers['date'])

        return True

    @property
    def is_kernelci_stable_rc_build_report(self):
        """ Determine whether or not mail is a kernelci build report for a stable-rc branch """
        # Subject: stable-rc/linux-4.9.y boot: 51 boots: 0 failed, 50 passed with 1 untried/unknown (v4.9.173-61-g43d95ffd279c)
        headers = Parser(policy=default).parsestr(self.contents)
        self.subject = headers['subject']

        try:
            m = kernelci_stable_rc_re.match(self.subject)
        except:
            return False
        if not m:
            return False

        n = re.match('v(\d+)\.(\d+)\.(\d+)-(\d+)-g.*', m.group(1))
        # Add 1 to the version number because this is a git-describe. The actual
        # kernel tag that will result will be the git describe tag plus 1.
        self.stable_rc_version = "{}.{}.{}".format(n.group(1), n.group(2), int(n.group(3))+1)
        self.stable_patch_count = int(n.group(4))-1

        self.mail_date = parsedate_to_datetime(headers['date'])

        return True


kernelci_mails = []
stable_rc_mails = []
for root, dirs, files in os.walk(lists_stable):
    for file in files:
        with open(os.path.join(root, file), 'rb') as f:
            mail = mail_message(f.read())
            if mail.is_stable_review:
                stable_rc_mails.append(mail)
            if mail.is_kernelci_stable_rc_build_report:
                kernelci_mails.append(mail)

print("{} stable-rc announcements found".format(len(stable_rc_mails)))
print("{} kernelci stable-rc build results found".format(len(kernelci_mails)))

dates = []
datediffs = []
for gmail in stable_rc_mails:
    found = False
    for kmail in kernelci_mails:
        if ((gmail.stable_rc_version == kmail.stable_rc_version) and
            (gmail.stable_patch_count == kmail.stable_patch_count)):
            found = True
            #print(gmail.stable_rc_version, kmail.mail_date-gmail.mail_date)
            print(gmail.mail_date.timestamp(), gmail.stable_rc_version, (kmail.mail_date-gmail.mail_date).total_seconds()/3600)
            dates.append(gmail.mail_date.timestamp())
            datediffs.append((kmail.mail_date-gmail.mail_date).total_seconds()/3600)
    #if not found:
    #    print("No kernelci build email found for {}/{}".format(gmail.stable_rc_version, gmail.stable_patch_count))

trace = go.Scatter(x = dates, y = datediffs)
data = [trace]
py.plot(data, filename='kernelci_stats')
