mkdir -p linux
test -d linux/mainline || git clone --reference /home/drue/src/linux/mainline git://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git linux/mainline
(cd linux/mainline && git remote get-url hikey || git remote add hikey https://git.linaro.org/lkft/arm64-stable-rc.git)
(cd linux/mainline && git remote get-url next || git remote add next git://git.kernel.org/pub/scm/linux/kernel/git/next/linux-next.git)
(cd linux/mainline && git remote get-url stable || git remote add stable git://git.kernel.org/pub/scm/linux/kernel/git/stable/linux-stable.git)
(cd linux/mainline && git remote get-url stable-rc || git remote add stable-rc git://git.kernel.org/pub/scm/linux/kernel/git/stable/linux-stable-rc.git)
(cd linux/mainline && git fetch --all --tags)
(cd linux/mainline && git worktree add -b next ../next next/master)
(cd linux/mainline && git worktree add -b 4.19 ../4.19 stable/linux-4.19.y)
(cd linux/mainline && git worktree add -b 4.14 ../4.14 stable/linux-4.14.y)
(cd linux/mainline && git worktree add -b 4.9 ../4.9 stable/linux-4.9.y)
(cd linux/mainline && git worktree add -b 4.4 ../4.4 stable/linux-4.4.y)
(cd linux/mainline && git worktree add -b hikey-4.4-rc ../hikey-4.4-rc hikey/4.4.y-rc-hikey)
