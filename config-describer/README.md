Provide a concise way to describe the contents of a Linux kernel config file.
Count up the number of "Y"'s, "N"'s, and "M"'s, and calculate a short sha sum.
Concatenate in the format `y<Y_COUNT>-m<M_COUNT>-n<N_COUNT>-s<SHA>`.

This is intentionally similar to the format of `git describe`.

# Implementation
```
$ cat describe.sh
Y_COUNT=$(grep -c "=y$" $1)
N_COUNT=$(grep -c "is not set$" $1)
M_COUNT=$(grep -c "=m$" $1)
SHA=$(sha256sum $1 | cut -c-12)

echo "y${Y_COUNT}-m${M_COUNT}-n${N_COUNT}-s${SHA}"
```

# Examples

```
$ describe.sh arm64-allmodconfig.config
y3954-m7392-n116-sb650e98ffff6
$ describe.sh arm64-allnoconfig.config
y310-m0-n487-s5b1396a578cd
$ describe.sh arm64-allyesconfig.config
y11548-m55-n123-s82f7c03fd5be
$ describe.sh arm64-defconfig.config
y2363-m555-n3979-s4dc1ccbc556a
$ describe.sh arm64-tinyconfig.config
y308-m0-n483-sdef367a531eb
$ describe.sh x86_64-allmodconfig.config
y3960-m7793-n125-s38ed845bf3a6
$ describe.sh x86_64-allnoconfig.config
y282-m0-n410-s95804210f152
$ describe.sh x86_64-allyesconfig.config
y11760-m58-n138-s91d9b09bb8e6
$ describe.sh x86_64-defconfig.config
y1323-m13-n2417-s063c231495e6
$ describe.sh x86_64-tinyconfig.config
y279-m0-n407-sb12781211a13

$ sh describe.sh /boot/config-5.8.10-200.fc32.x86_64
y2325-m3594-n1785-s255fba8b9e32
```

# Generating the configs

```
tuxbuild build-set --git-repo 'https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git' --git-ref v5.9 --tux-config buildset.yaml --set-name config-combos --json-out out.json
curl -o arm64-allnoconfig.config -Ls https://builds.tuxbuild.com/D7m_NwG2i_i21VsFhl46sA/kernel.config
curl -o arm64-allyesconfig.config -Ls https://builds.tuxbuild.com/YP68piYpbbZh8YtoGBoFVA/kernel.config
curl -o arm64-allmodconfig.config -Ls https://builds.tuxbuild.com/wmMqM7Midg_qgrZJopNoIw/kernel.config
curl -o arm64-tinyconfig.config -Ls https://builds.tuxbuild.com/Y_tcnmdV0KiFDVRQuN8FtQ/kernel.config
curl -o arm64-defconfig.config -Ls https://builds.tuxbuild.com/hG415RL4sTWS1h1kTPcVuA/kernel.config
curl -o x86_64-allnoconfig.config -Ls https://builds.tuxbuild.com/n-nxXKim_jJDWgFnZ9Oi6w/kernel.config
curl -o x86_64-allyesconfig.config -Ls https://builds.tuxbuild.com/ZOTND9mgTqm0dI8xtmi4UA/kernel.config
curl -o x86_64-allmodconfig.config -Ls https://builds.tuxbuild.com/-AMnXwuBSgZrkLgUS1PxwQ/kernel.config
curl -o x86_64-tinyconfig.config -Ls https://builds.tuxbuild.com/ekpamhS6DDR8_bBlEFWHww/kernel.config
curl -o x86_64-defconfig.config -Ls https://builds.tuxbuild.com/k0Lqtj16nqSriyv0cP2K5w/kernel.config
for i in `ls *.config`; do echo "$ describe.sh $i"; sh describe.sh $i; done
```
