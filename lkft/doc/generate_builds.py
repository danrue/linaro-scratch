from tabulate import tabulate

class Board(object):
    def __init__(self, name, architecture, jenkins_name):
        self.name = name
        self.architecture = architecture
        self.jenkins_name = jenkins_name

class Branch(object):
    def __init__(self, name, squad_name, jenkins_name):
        self.name = name
        self.squad_name = squad_name
        self.jenkins_name = jenkins_name

class BoardxBranch(object):
    def __init__(self, board, branch):
        self.board = board
        self.Branch = branch

    def jenkins_badge_url(self):
        return "https://ci.linaro.org/buildStatus/icon?job=openembedded-lkft-linux-{}/DISTRO=rpb,MACHINE={},label=docker-lkft".format(branch.jenkins_name, board.jenkins_name)

    def jenkins_build_url(self):
        return "https://ci.linaro.org/view/lkft/job/openembedded-lkft-linux-{}/DISTRO=rpb,MACHINE={},label=docker-lkft/".format(branch.jenkins_name, board.jenkins_name),

    def squad_badge_url(self):
        return "squad_favicon.png"
    def squad_project_url(self):
        return "https://qa-reports.linaro.org/lkft/linux-{}/".format(branch.squad_name)


boards = [
    # pretty name, architecture, jenkins MACHINE name
    Board('hikey', 'arm64', 'hikey'),
    Board('x15', 'arm', 'am57xx-evm'),
    Board('juno', 'arm64', 'juno'),
    Board('dell', 'x86_64', 'intel-core2-32'),
]
branches = [
    # pretty name, squad name, jenkins name
    Branch('4.14 LTS', 'stable-4.14-oe', 'stable-4.14'),
    Branch('4.14-rc LTS', 'stable-rc-4.14-oe', 'stable-rc-4.14'),
    Branch('4.9 LTS', 'stable-4.9-oe', 'stable-rc-4.9'),
    Branch('4.9-rc LTS', 'stable-rc-4.9-oe', 'stable-rc-4.9'),
    Branch('4.4 LTS', 'stable-4.4-oe', 'stable-rc-4.4'),
    Branch('4.4-rc LTS', 'stable-rc-4.4-oe', 'stable-rc-4.4'),
]

table = []
for board in boards:
    row = []
    row.append(board.name)
    row.append(board.architecture)
    for branch in branches:
        rowdata = BoardxBranch(board, branch)
        # Append a row to the table
        row.append(
            '<a href="{}"><img src="{}" /></a><br /><a href="{}"><img src="{}" /></a>'.format( # html
            rowdata.jenkins_build_url(),
            rowdata.jenkins_badge_url(),
            rowdata.squad_project_url(),
            rowdata.squad_badge_url(),
            )
        )
    table.append(row)

headers = ['Board', 'Architecture']
for branch in branches:
    headers.append(branch.name)

print(tabulate(table, headers=headers, tablefmt="html"))
