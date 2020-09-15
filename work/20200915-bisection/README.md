# tuxmake

```
dan.rue@hackbox2:~/linux-stable-rc$ git bisect start
dan.rue@hackbox2:~/linux-stable-rc$ git bisect bad
dan.rue@hackbox2:~/linux-stable-rc$ git bisect good v5.4.65
dan.rue@hackbox2:~/linux-stable-rc$ git bisect run tuxmake -r docker -a arm64
```

# tuxbuild

```
drue@nuc:~/src/linux-stable-rc$ git bisect start --no-checkout
drue@nuc:~/src/linux-stable-rc$ git bisect bad
drue@nuc:~/src/linux-stable-rc$ git bisect good v5.4.65
drue@nuc:~/src/linux-stable-rc$ git bisect run sh -c 'tuxbuild build-set --git-repo https://gitlab.com/Linaro/lkft/mirrors/stable/linux-stable-rc --git-sha $(cat .git/BISECT_HEAD) --tux-config https://gitlab.com/Linaro/lkft/pipelines/lkft-common/-/raw/master/tuxconfig.yml --set-name arm64-gcc-9'
```
