from tabulate import tabulate

class Branch(object):
    def __init__(self, name, squad_name, jenkins_name, label="docker-lkft"):
        self.name = name
        self.squad_name = squad_name
        self.jenkins_name = jenkins_name
        self.label = label
    def get_name(self):
        return self.name
    def get_squad_name(self):
        return self.squad_name
    def get_jenkins_name(self):
        return self.jenkins_name
    def get_label(self):
        return self.label

class Board(object):
    def __init__(self, name, architecture, jenkins_name):
        self.name = name
        self.architecture = architecture
        self.jenkins_name = jenkins_name
        self.branches = [
            # pretty name, squad name, jenkins name
            Branch('4.14 LTS',
                   'linux-stable-4.14-oe',
                   'openembedded-lkft-linux-stable-4.14'
                  ),
            Branch('4.14-rc LTS',
                   'linux-stable-rc-4.14-oe',
                   'openembedded-lkft-linux-stable-rc-4.14'
                  ),
            Branch('4.9 LTS',
                   'linux-stable-4.9-oe',
                   'openembedded-lkft-linux-stable-rc-4.9'
                  ),
            Branch('4.9-rc LTS',
                   'linux-stable-rc-4.9-oe',
                   'openembedded-lkft-linux-stable-rc-4.9'
                  ),
            Branch('4.4 LTS',
                   'linux-stable-4.4-oe',
                   'openembedded-lkft-linux-stable-rc-4.4',
                  ),
            Branch('4.4-rc LTS',
                   'linux-stable-rc-4.4-oe',
                   'openembedded-lkft-linux-stable-rc-4.4',
                  ),
        ]
    def get_name(self):
        return self.name
    def get_architecture(self):
        return self.architecture
    def get_jenkins_name(self):
        return self.jenkins_name
    def get_branches(self):
        return iter(self.branches)

    def jenkins_badge_url(self, branch):
        # openembedded-lkft-linaro-hikey-stable-4.4/DISTRO=rpb,MACHINE=hikey,label=docker-stretch-amd64/
        return "https://ci.linaro.org/buildStatus/icon?job={}/DISTRO=rpb,MACHINE={},label={}".format(branch.get_jenkins_name(), self.get_jenkins_name(), branch.get_label())

    def jenkins_build_url(self, branch):
        return "https://ci.linaro.org/view/lkft/job/{}/DISTRO=rpb,MACHINE={},label=docker-lkft/".format(branch.get_jenkins_name(), self.get_jenkins_name()),

    def squad_badge_url(self):
        return "squad_favicon.png"
    def squad_project_url(self, branch):
        return "https://qa-reports.linaro.org/lkft/{}/".format(branch.get_squad_name())


class BoardHikey(Board):
    def __init__(self):
        super().__init__("hikey", "arm64", "hikey")
        self.branches = [
            # pretty name, squad name, jenkins name
            Branch('4.14 LTS',
                   'linux-stable-4.14-oe',
                   'openembedded-lkft-linux-stable-4.14'
                  ),
            Branch('4.14-rc LTS',
                   'linux-stable-rc-4.14-oe',
                   'openembedded-lkft-linux-stable-rc-4.14'
                  ),
            Branch('4.9 LTS',
                   'linux-stable-4.9-oe',
                   'openembedded-lkft-linux-stable-rc-4.9'
                  ),
            Branch('4.9-rc LTS',
                   'linux-stable-rc-4.9-oe',
                   'openembedded-lkft-linux-stable-rc-4.9'
                  ),
            Branch('Linaro Hikey 4.4 LTS',
                   'linaro-hikey-stable-4.4-oe',
                   'openembedded-lkft-linaro-hikey-stable-4.4',
                   label="docker-stretch-amd64"
                  ),
            Branch('Linaro Hikey 4.4-rc LTS',
                   'linaro-hikey-stable-rc-4.4-oe',
                   'openembedded-lkft-linaro-hikey-stable-rc-4.4',
                   label="docker-stretch-amd64"
                  ),
        ]
class BoardX15(Board):
    def __init__(self):
        super().__init__("x15", "arm", "am57xx-evm")
class BoardJuno(Board):
    def __init__(self):
        super().__init__("juno", "arm64", "juno")
class BoardDell(Board):
    def __init__(self):
        super().__init__("dell", "x86_64", "intel-core2-32")


boards = [
    # pretty name, architecture, jenkins MACHINE name
    BoardHikey(),
    BoardX15(),
    BoardJuno(),
    BoardDell(),
]

table = []
for board in boards:
    row = []
    row.append(board.get_name())
    row.append(board.get_architecture())
    for branch in board.get_branches():
        # Append a row to the table
        row.append(
            '<a href="{}"><img src="{}" /></a><br /><a href="{}"><img src="{}" /></a>'.format( # html
            board.jenkins_build_url(branch),
            board.jenkins_badge_url(branch),
            board.squad_project_url(branch),
            board.squad_badge_url(),
            )
        )
    table.append(row)

headers = ['Board', 'Architecture']
for branch in BoardX15().get_branches():
    headers.append(branch.get_name())

print(tabulate(table, headers=headers, tablefmt="html"))
