#!/usr/bin/env python3

# Utility script to modify the display of email in mutt.
#
# Installation:
#   In muttrc, set the following:
#     set display_filter="$HOME/.mutt/display_filter.py"
#
# This script contains the following functions:
#   X-Date: Add an X-Date header, which is Date translated to localtime
#   X-URI: Add an X-URI header, which is added when lore-compatible mail is
#          found

import sys
import email

from email.utils import mktime_tz, parsedate_tz, formatdate
from collections import OrderedDict

class muttemail:

    def __init__(self, raw_message):
       self.message = email.message_from_string(raw_message)

    def as_string(self):
       return self.message.as_string()

    def create_xdate_header(self):
        ''' Add an X-Date header, which is Date converted to localtime. '''
        date = self.message.get('Date', None)
        if not date:
            return

        tz_tuple = parsedate_tz(date)
        epoch_time = mktime_tz(tz_tuple)
        self.message.add_header('X-Date', formatdate(epoch_time, localtime=True))

    def create_xuri_header(self):
        '''
        If the mail is sent to a lore-supported mailing list, provide a header
        with a lore link directly.
        '''

        # In order of preference; first match wins
        lore_lists = OrderedDict({
            'linux-kernel@vger.kernel.org': 'https://lore.kernel.org/lkml/',
            'backports@vger.kernel.org': 'https://lore.kernel.org/backports/',
            'cocci@systeme.lip6.fr': 'https://lore.kernel.org/cocci/',
            'kernelnewbies@kernelnewbies.org': 'https://lore.kernel.org/kernelnewbies/',
            'linux-arm-kernel@lists.infradead.org': 'https://lore.kernel.org/linux-arm-kernel/',
            'linux-block@vger.kernel.org': 'https://lore.kernel.org/linux-block/',
            'linux-bluetooth@vger.kernel.org': 'https://lore.kernel.org/linux-bluetooth/',
            'linux-btrfs@vger.kernel.org': 'https://lore.kernel.org/linux-btrfs/',
            'linux-clk@vger.kernel.org': 'https://lore.kernel.org/linux-clk/',
            'linux-integrity@vger.kernel.org': 'https://lore.kernel.org/linux-integrity/',
            'linux-nfs@vger.kernel.org': 'https://lore.kernel.org/linux-nfs/',
            'linux-parisc@vger.kernel.org': 'https://lore.kernel.org/linux-parisc/',
            'linux-pci@vger.kernel.org': 'https://lore.kernel.org/linux-pci/',
            'linux-riscv@lists.infradead.org': 'https://lore.kernel.org/linux-riscv/',
            'linux-rtc@vger.kernel.org': 'https://lore.kernel.org/linux-rtc/',
            'linux-security-module@vger.kernel.org': 'https://lore.kernel.org/linux-security-module/',
            'linux-sgx@vger.kernel.org': 'https://lore.kernel.org/linux-sgx/',
            'linux-wireless@vger.kernel.org': 'https://lore.kernel.org/linux-wireless/',
            'linuxppc-dev@lists.ozlabs.org': 'https://lore.kernel.org/linuxppc-dev/',
            'selinux@vger.kernel.org': 'https://lore.kernel.org/selinux/',
            'selinux-refpolicy@vger.kernel.org': 'https://lore.kernel.org/selinux-refpolicy/',
            'util-linux@vger.kernel.org': 'https://lore.kernel.org/util-linux/',
            'wireguard@lists.zx2c4.com': 'https://lore.kernel.org/wireguard/',
        })
        message_id = self.message.get('Message-ID', None)
        if not message_id:
            return
        recipients = self.message.get('To', '') + ' ' + self.message.get('Cc', '')
        for email_list, lore_url in lore_lists.items():
            if email_list in recipients:
                self.message.add_header('X-URI', lore_url+message_id[1:-1])
                return

if __name__ == '__main__':
    email = muttemail(sys.stdin.read())
    email.create_xdate_header()
    email.create_xuri_header()
    sys.stdout.write(email.as_string())