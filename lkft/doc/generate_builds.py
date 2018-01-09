from tabulate import tabulate

class Board(object):
    def __init__(self, name, architecture, jenkins_name):
        self.name = name
        self.architecture = architecture
        self.jenkins_name = jenkins_name
    def get_name(self):
        return self.name
    def get_architecture(self):
        return self.architecture
    def get_jenkins_name(self):
        return self.jenkins_name
    #openembedded-lkft-linaro-hikey-stable-rc-4.4

class BoardHikey(Board):
    def __init__(self):
        super().__init__("hikey", "arm64", "hikey")
class BoardX15(Board):
    def __init__(self):
        super().__init__("x15", "arm", "am57xx-evm")
class BoardJuno(Board):
    def __init__(self):
        super().__init__("juno", "arm64", "juno")
class BoardDell(Board):
    def __init__(self):
        super().__init__("dell", "x86_64", "intel-core2-32")


class Branch(object):
    def __init__(self, name, squad_name, jenkins_name):
        self.name = name
        self.squad_name = squad_name
        self.jenkins_name = jenkins_name
    def get_name(self):
        return self.name
    def get_squad_name(self):
        return self.squad_name
    def get_jenkins_name(self):
        return self.jenkins_name

class BoardxBranch(object):
    def __init__(self, board, branch):
        self.board = board
        self.Branch = branch

    def jenkins_badge_url(self):
        return "https://ci.linaro.org/buildStatus/icon?job=openembedded-lkft-linux-{}/DISTRO=rpb,MACHINE={},label=docker-lkft".format(branch.get_jenkins_name(), board.get_jenkins_name())

    def jenkins_build_url(self):
        return "https://ci.linaro.org/view/lkft/job/openembedded-lkft-linux-{}/DISTRO=rpb,MACHINE={},label=docker-lkft/".format(branch.get_jenkins_name(), board.get_jenkins_name()),

    def squad_badge_url(self):
        return "squad_favicon.png"
    def squad_project_url(self):
        return "https://qa-reports.linaro.org/lkft/linux-{}/".format(branch.get_squad_name())


boards = [
    # pretty name, architecture, jenkins MACHINE name
    BoardHikey(),
    BoardX15(),
    BoardJuno(),
    BoardDell(),
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
    row.append(board.get_name())
    row.append(board.get_architecture())
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
    headers.append(branch.get_name())

print(tabulate(table, headers=headers, tablefmt="html"))
