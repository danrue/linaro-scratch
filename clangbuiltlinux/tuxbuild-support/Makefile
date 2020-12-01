builds.json: all_clang.yaml
	tuxbuild build-set --git-repo 'https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git' --git-ref master --tux-config all_clang.yaml --set-name all --json-out builds.json

all_clang.yaml:
	python3 buildset.py > all_clang.yaml
