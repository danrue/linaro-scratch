from tabulate import tabulate

boards = [
    # pretty name, architecture, jenkins MACHINE name
    ('hikey', 'arm64', 'hikey'),
    ('x15', 'arm', 'am57xx-evm'),
    ('dell', 'x86_64', 'intel-core2-32'),
]
branches = [
    # pretty name, squad name, jenkins name
    ('4.14 LTS', 'stable-4.14-oe', 'stable-4.14'),
    ('4.14-rc LTS', 'stable-rc-4.14-oe', 'stable-rc-4.14'),
    ('4.9 LTS', 'stable-4.9-oe', 'stable-rc-4.9'),
    ('4.9-rc LTS', 'stable-rc-4.9-oe', 'stable-rc-4.9'),
]

table = []
for board in boards:
    row = []
    row.append(board[0]) # board pretty name is first column
    row.append(board[1]) # board architecture is second column
    for branch in branches:
        # Append a row to the table
        row.append(
            #"![{}]({})<br />![{}]({})".format( # markdown
            '<a href="{}"><img src="{}" /></a><br /><a href="{}"><img src="{}" /></a>'.format( # html
                "https://ci.linaro.org/view/lkft/job/openembedded-lkft-linux-{}/DISTRO=rpb,MACHINE={},label=docker-lkft/".format(branch[2], board[2]),
                "https://ci.linaro.org/buildStatus/icon?job=openembedded-lkft-linux-{}/DISTRO=rpb,MACHINE={},label=docker-lkft".format(branch[2], board[2]),
                "https://qa-reports.linaro.org/lkft/linux-{}/".format(branch[1]),
                "squad_favicon.png",
            )
        )
    table.append(row)

headers = ['Board', 'Architecture']
for branch in branches:
    headers.append(branch[0])

print(tabulate(table, headers=headers, tablefmt="html"))
