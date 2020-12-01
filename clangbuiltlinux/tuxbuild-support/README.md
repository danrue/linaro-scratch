# Clang Support in Tuxbuild

As of 2020-12-01, the following architectures were built with clang-11 and
clang-nightly using tinyconfig and mainline tag 5.10-rc6.

```
empty = not supported
pass = working with tinyconfig
fail = fail with tinyconfig
```

9 failures

|               | arc | arm | arm64 | i386 | mips | parisc | powerpc | riscv | s390 | sh  | sparc | x86_64 |
| ------------- | --- | --- | ----- | ---- | ---- | ------ | ------- | ----- | ---- | --- | ----- | ------ |
| clang-10      |     | yes | yes   | yes  | fail |        | fail    | pass  | pass |     | fail  | yes    |
| clang-11      |     | yes | yes   | yes  | fail |        | fail    | pass  | pass |     | fail  | yes    |
| clang-nightly |     | yes | yes   | yes  | fail |        | fail    | pass  | pass |     | fail  | yes    |


Build log (links go to actual log of each build):

```
$ tuxbuild build-set --git-repo 'https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git' --git-ref master --tux-config all_clang.yaml --set-name all --json-out builds.json
Building Linux Kernel build set all
⏳ Queued:  i386 (tinyconfig) with clang-10 @ https://builds.tuxbuild.com/1l4Z9PL5AWEa3h1qL0ZTli2A14w/
⏳ Queued:  x86 (tinyconfig) with clang-10 @ https://builds.tuxbuild.com/1l4Z9NdxgYcVsPUVFD1wrfIlr6G/
⏳ Queued:  x86_64 (tinyconfig) with clang-10 @ https://builds.tuxbuild.com/1l4Z9Rwc65CiWJIqEobs7hfjk1n/
⏳ Queued:  arm (tinyconfig) with clang-10 @ https://builds.tuxbuild.com/1l4Z9NCKAXl42lQIQkHctUQcZsB/
⏳ Queued:  arm64 (tinyconfig) with clang-10 @ https://builds.tuxbuild.com/1l4Z9R805u2FKuZkxM9vGrNVrF0/
⏳ Queued:  mips (tinyconfig) with clang-10 @ https://builds.tuxbuild.com/1l4Z9SW4Oox98j3fsSDzYOVMSY8/
⏳ Queued:  riscv (tinyconfig) with clang-10 @ https://builds.tuxbuild.com/1l4Z9LsIPpkJrLVXdASvfghq6jI/
⏳ Queued:  s390 (tinyconfig) with clang-10 @ https://builds.tuxbuild.com/1l4Z9NqWhv0LGyEEad8WXbfGkzG/
⏳ Queued:  powerpc (tinyconfig) with clang-10 @ https://builds.tuxbuild.com/1l4Z9QwIYq32zZgHf1QMpDkynpd/
⏳ Queued:  sparc (tinyconfig) with clang-10 @ https://builds.tuxbuild.com/1l4Z9O8akZHyOcw3x2h10MQQBHK/
⏳ Queued:  i386 (tinyconfig) with clang-11 @ https://builds.tuxbuild.com/1l4Z9MsDbMT7CcxmL3EvbNSRdwB/
⏳ Queued:  x86 (tinyconfig) with clang-11 @ https://builds.tuxbuild.com/1l4Z9QWCCZ2pvdSebkKILzA7vWy/
⏳ Queued:  x86_64 (tinyconfig) with clang-11 @ https://builds.tuxbuild.com/1l4Z9SfpqTo1ad5lzgQpZJ8vA9o/
⏳ Queued:  arm (tinyconfig) with clang-11 @ https://builds.tuxbuild.com/1l4Z9OjBrV3qm4mN5JPOZrNKSwc/
⏳ Queued:  arm64 (tinyconfig) with clang-11 @ https://builds.tuxbuild.com/1l4Z9S209l1yjSJIFQz7RvyWfRK/
⏳ Queued:  mips (tinyconfig) with clang-11 @ https://builds.tuxbuild.com/1l4Z9Pk75sWu6NQcKioINksN8Uu/
⏳ Queued:  riscv (tinyconfig) with clang-11 @ https://builds.tuxbuild.com/1l4Z9NNDSQMOIRX1FtwqNVYPm7k/
⏳ Queued:  s390 (tinyconfig) with clang-11 @ https://builds.tuxbuild.com/1l4Z9Pt9zFO761TnAfagFQHDvHI/
⏳ Queued:  powerpc (tinyconfig) with clang-11 @ https://builds.tuxbuild.com/1l4Z9QSuVMxQOUdZuNFzR02bxg9/
⏳ Queued:  sparc (tinyconfig) with clang-11 @ https://builds.tuxbuild.com/1l4Z9NvEKs1l6snITnZvEFfNNpi/
⏳ Queued:  i386 (tinyconfig) with clang-nightly @ https://builds.tuxbuild.com/1l4Z9On6HdjBo1MAsgrez2YoDJw/
⏳ Queued:  x86 (tinyconfig) with clang-nightly @ https://builds.tuxbuild.com/1l4Z9S5RWfoyKuoIZfPT9d4JKqm/
⏳ Queued:  x86_64 (tinyconfig) with clang-nightly @ https://builds.tuxbuild.com/1l4Z9N6jiKf7fjfsqtQdasV72t5/
⏳ Queued:  arm (tinyconfig) with clang-nightly @ https://builds.tuxbuild.com/1l4Z9RzOrjmaymaYYhyRZ16l5so/
⏳ Queued:  arm64 (tinyconfig) with clang-nightly @ https://builds.tuxbuild.com/1l4Z9Q2BEDoPO5ssGjMmHPuTJvU/
⏳ Queued:  mips (tinyconfig) with clang-nightly @ https://builds.tuxbuild.com/1l4Z9RorkzBecrgcjm4Kw80SH6q/
⏳ Queued:  riscv (tinyconfig) with clang-nightly @ https://builds.tuxbuild.com/1l4Z9NFMlFUgKbg0sNXBAJh2HYV/
⏳ Queued:  s390 (tinyconfig) with clang-nightly @ https://builds.tuxbuild.com/1l4Z9RiOFmx5nVrwfGrLEwRmJQV/
⏳ Queued:  powerpc (tinyconfig) with clang-nightly @ https://builds.tuxbuild.com/1l4Z9RhN8Q521ENnerYGdjpUnHF/
⏳ Queued:  sparc (tinyconfig) with clang-nightly @ https://builds.tuxbuild.com/1l4Z9OvqJuMfIg8VFDCxEULIaNj/
⚗️  Building: b65054597872 ("Linux 5.10-rc6") i386 (tinyconfig) with clang-10 @ https://builds.tuxbuild.com/1l4Z9PL5AWEa3h1qL0ZTli2A14w/
⚗️  Building: b65054597872 ("Linux 5.10-rc6") x86 (tinyconfig) with clang-10 @ https://builds.tuxbuild.com/1l4Z9NdxgYcVsPUVFD1wrfIlr6G/
⚗️  Building: b65054597872 ("Linux 5.10-rc6") x86_64 (tinyconfig) with clang-10 @ https://builds.tuxbuild.com/1l4Z9Rwc65CiWJIqEobs7hfjk1n/
⚗️  Building: b65054597872 ("Linux 5.10-rc6") arm (tinyconfig) with clang-10 @ https://builds.tuxbuild.com/1l4Z9NCKAXl42lQIQkHctUQcZsB/
⚗️  Building: b65054597872 ("Linux 5.10-rc6") x86_64 (tinyconfig) with clang-11 @ https://builds.tuxbuild.com/1l4Z9SfpqTo1ad5lzgQpZJ8vA9o/
⚗️  Building: b65054597872 ("Linux 5.10-rc6") arm64 (tinyconfig) with clang-10 @ https://builds.tuxbuild.com/1l4Z9R805u2FKuZkxM9vGrNVrF0/
⚗️  Building: b65054597872 ("Linux 5.10-rc6") powerpc (tinyconfig) with clang-10 @ https://builds.tuxbuild.com/1l4Z9QwIYq32zZgHf1QMpDkynpd/
⚗️  Building: b65054597872 ("Linux 5.10-rc6") mips (tinyconfig) with clang-10 @ https://builds.tuxbuild.com/1l4Z9SW4Oox98j3fsSDzYOVMSY8/
⚗️  Building: b65054597872 ("Linux 5.10-rc6") arm (tinyconfig) with clang-11 @ https://builds.tuxbuild.com/1l4Z9OjBrV3qm4mN5JPOZrNKSwc/
⚗️  Building: b65054597872 ("Linux 5.10-rc6") s390 (tinyconfig) with clang-11 @ https://builds.tuxbuild.com/1l4Z9Pt9zFO761TnAfagFQHDvHI/
⚗️  Building: b65054597872 ("Linux 5.10-rc6") riscv (tinyconfig) with clang-10 @ https://builds.tuxbuild.com/1l4Z9LsIPpkJrLVXdASvfghq6jI/
⚗️  Building: b65054597872 ("Linux 5.10-rc6") x86 (tinyconfig) with clang-11 @ https://builds.tuxbuild.com/1l4Z9QWCCZ2pvdSebkKILzA7vWy/
⚗️  Building: b65054597872 ("Linux 5.10-rc6") riscv (tinyconfig) with clang-11 @ https://builds.tuxbuild.com/1l4Z9NNDSQMOIRX1FtwqNVYPm7k/
⚗️  Building: b65054597872 ("Linux 5.10-rc6") i386 (tinyconfig) with clang-nightly @ https://builds.tuxbuild.com/1l4Z9On6HdjBo1MAsgrez2YoDJw/
⚗️  Building: b65054597872 ("Linux 5.10-rc6") x86 (tinyconfig) with clang-nightly @ https://builds.tuxbuild.com/1l4Z9S5RWfoyKuoIZfPT9d4JKqm/
⚗️  Building: b65054597872 ("Linux 5.10-rc6") mips (tinyconfig) with clang-11 @ https://builds.tuxbuild.com/1l4Z9Pk75sWu6NQcKioINksN8Uu/
⚗️  Building: b65054597872 ("Linux 5.10-rc6") i386 (tinyconfig) with clang-11 @ https://builds.tuxbuild.com/1l4Z9MsDbMT7CcxmL3EvbNSRdwB/
⚗️  Building: b65054597872 ("Linux 5.10-rc6") s390 (tinyconfig) with clang-10 @ https://builds.tuxbuild.com/1l4Z9NqWhv0LGyEEad8WXbfGkzG/
⚗️  Building: b65054597872 ("Linux 5.10-rc6") arm64 (tinyconfig) with clang-11 @ https://builds.tuxbuild.com/1l4Z9S209l1yjSJIFQz7RvyWfRK/
⚗️  Building: b65054597872 ("Linux 5.10-rc6") sparc (tinyconfig) with clang-11 @ https://builds.tuxbuild.com/1l4Z9NvEKs1l6snITnZvEFfNNpi/
⚗️  Building: b65054597872 ("Linux 5.10-rc6") powerpc (tinyconfig) with clang-11 @ https://builds.tuxbuild.com/1l4Z9QSuVMxQOUdZuNFzR02bxg9/
⚗️  Building: b65054597872 ("Linux 5.10-rc6") sparc (tinyconfig) with clang-10 @ https://builds.tuxbuild.com/1l4Z9O8akZHyOcw3x2h10MQQBHK/
🎉 Pass: b65054597872 ("Linux 5.10-rc6") i386 (tinyconfig) with clang-10 @ https://builds.tuxbuild.com/1l4Z9PL5AWEa3h1qL0ZTli2A14w/
⚗️  Building: b65054597872 ("Linux 5.10-rc6") x86_64 (tinyconfig) with clang-nightly @ https://builds.tuxbuild.com/1l4Z9N6jiKf7fjfsqtQdasV72t5/
👹 Fail (12 errors) with status message 'failure while building tuxmake target(s): kernel debugkernel': b65054597872 ("Linux 5.10-rc6") sparc (tinyconfig) with clang-10 @ https://builds.tuxbuild.com/1l4Z9O8akZHyOcw3x2h10MQQBHK/
⚗️  Building: b65054597872 ("Linux 5.10-rc6") arm (tinyconfig) with clang-nightly @ https://builds.tuxbuild.com/1l4Z9RzOrjmaymaYYhyRZ16l5so/
⚗️  Building: b65054597872 ("Linux 5.10-rc6") riscv (tinyconfig) with clang-nightly @ https://builds.tuxbuild.com/1l4Z9NFMlFUgKbg0sNXBAJh2HYV/
⚗️  Building: b65054597872 ("Linux 5.10-rc6") arm64 (tinyconfig) with clang-nightly @ https://builds.tuxbuild.com/1l4Z9Q2BEDoPO5ssGjMmHPuTJvU/
⚗️  Building: b65054597872 ("Linux 5.10-rc6") mips (tinyconfig) with clang-nightly @ https://builds.tuxbuild.com/1l4Z9RorkzBecrgcjm4Kw80SH6q/
🎉 Pass: b65054597872 ("Linux 5.10-rc6") arm (tinyconfig) with clang-10 @ https://builds.tuxbuild.com/1l4Z9NCKAXl42lQIQkHctUQcZsB/
⚗️  Building: b65054597872 ("Linux 5.10-rc6") s390 (tinyconfig) with clang-nightly @ https://builds.tuxbuild.com/1l4Z9RiOFmx5nVrwfGrLEwRmJQV/
👹 Fail (12 errors) with status message 'failure while building tuxmake target(s): kernel debugkernel': b65054597872 ("Linux 5.10-rc6") sparc (tinyconfig) with clang-11 @ https://builds.tuxbuild.com/1l4Z9NvEKs1l6snITnZvEFfNNpi/
👾 Pass (1 warning): b65054597872 ("Linux 5.10-rc6") x86 (tinyconfig) with clang-10 @ https://builds.tuxbuild.com/1l4Z9NdxgYcVsPUVFD1wrfIlr6G/
⚗️  Building: b65054597872 ("Linux 5.10-rc6") powerpc (tinyconfig) with clang-nightly @ https://builds.tuxbuild.com/1l4Z9RhN8Q521ENnerYGdjpUnHF/
🎉 Pass: b65054597872 ("Linux 5.10-rc6") riscv (tinyconfig) with clang-10 @ https://builds.tuxbuild.com/1l4Z9LsIPpkJrLVXdASvfghq6jI/
⚗️  Building: b65054597872 ("Linux 5.10-rc6") sparc (tinyconfig) with clang-nightly @ https://builds.tuxbuild.com/1l4Z9OvqJuMfIg8VFDCxEULIaNj/
👹 Fail (0 errors) with status message 'failure while building tuxmake target(s): kernel debugkernel': b65054597872 ("Linux 5.10-rc6") mips (tinyconfig) with clang-10 @ https://builds.tuxbuild.com/1l4Z9SW4Oox98j3fsSDzYOVMSY8/
🎉 Pass: b65054597872 ("Linux 5.10-rc6") arm (tinyconfig) with clang-11 @ https://builds.tuxbuild.com/1l4Z9OjBrV3qm4mN5JPOZrNKSwc/
👹 Fail (58 errors) with status message 'failure while building tuxmake target(s): kernel debugkernel': b65054597872 ("Linux 5.10-rc6") powerpc (tinyconfig) with clang-11 @ https://builds.tuxbuild.com/1l4Z9QSuVMxQOUdZuNFzR02bxg9/
👹 Fail (0 errors) with status message 'failure while building tuxmake target(s): kernel debugkernel': b65054597872 ("Linux 5.10-rc6") mips (tinyconfig) with clang-11 @ https://builds.tuxbuild.com/1l4Z9Pk75sWu6NQcKioINksN8Uu/
🎉 Pass: b65054597872 ("Linux 5.10-rc6") s390 (tinyconfig) with clang-11 @ https://builds.tuxbuild.com/1l4Z9Pt9zFO761TnAfagFQHDvHI/
👾 Pass (3 warnings): b65054597872 ("Linux 5.10-rc6") arm64 (tinyconfig) with clang-10 @ https://builds.tuxbuild.com/1l4Z9R805u2FKuZkxM9vGrNVrF0/
👾 Pass (1 warning): b65054597872 ("Linux 5.10-rc6") x86_64 (tinyconfig) with clang-11 @ https://builds.tuxbuild.com/1l4Z9SfpqTo1ad5lzgQpZJ8vA9o/
👾 Pass (1 warning): b65054597872 ("Linux 5.10-rc6") x86_64 (tinyconfig) with clang-10 @ https://builds.tuxbuild.com/1l4Z9Rwc65CiWJIqEobs7hfjk1n/
👾 Pass (3 warnings): b65054597872 ("Linux 5.10-rc6") arm64 (tinyconfig) with clang-11 @ https://builds.tuxbuild.com/1l4Z9S209l1yjSJIFQz7RvyWfRK/
🎉 Pass: b65054597872 ("Linux 5.10-rc6") i386 (tinyconfig) with clang-nightly @ https://builds.tuxbuild.com/1l4Z9On6HdjBo1MAsgrez2YoDJw/
🎉 Pass: b65054597872 ("Linux 5.10-rc6") riscv (tinyconfig) with clang-11 @ https://builds.tuxbuild.com/1l4Z9NNDSQMOIRX1FtwqNVYPm7k/
👹 Fail (12 errors) with status message 'failure while building tuxmake target(s): kernel debugkernel': b65054597872 ("Linux 5.10-rc6") sparc (tinyconfig) with clang-nightly @ https://builds.tuxbuild.com/1l4Z9OvqJuMfIg8VFDCxEULIaNj/
🎉 Pass: b65054597872 ("Linux 5.10-rc6") riscv (tinyconfig) with clang-nightly @ https://builds.tuxbuild.com/1l4Z9NFMlFUgKbg0sNXBAJh2HYV/
👾 Pass (1 warning): b65054597872 ("Linux 5.10-rc6") x86 (tinyconfig) with clang-nightly @ https://builds.tuxbuild.com/1l4Z9S5RWfoyKuoIZfPT9d4JKqm/
👹 Fail (58 errors) with status message 'failure while building tuxmake target(s): kernel debugkernel': b65054597872 ("Linux 5.10-rc6") powerpc (tinyconfig) with clang-10 @ https://builds.tuxbuild.com/1l4Z9QwIYq32zZgHf1QMpDkynpd/
🎉 Pass: b65054597872 ("Linux 5.10-rc6") s390 (tinyconfig) with clang-10 @ https://builds.tuxbuild.com/1l4Z9NqWhv0LGyEEad8WXbfGkzG/
👾 Pass (1 warning): b65054597872 ("Linux 5.10-rc6") x86 (tinyconfig) with clang-11 @ https://builds.tuxbuild.com/1l4Z9QWCCZ2pvdSebkKILzA7vWy/
🎉 Pass: b65054597872 ("Linux 5.10-rc6") i386 (tinyconfig) with clang-11 @ https://builds.tuxbuild.com/1l4Z9MsDbMT7CcxmL3EvbNSRdwB/
👾 Pass (1 warning): b65054597872 ("Linux 5.10-rc6") x86_64 (tinyconfig) with clang-nightly @ https://builds.tuxbuild.com/1l4Z9N6jiKf7fjfsqtQdasV72t5/
🎉 Pass: b65054597872 ("Linux 5.10-rc6") arm (tinyconfig) with clang-nightly @ https://builds.tuxbuild.com/1l4Z9RzOrjmaymaYYhyRZ16l5so/
👹 Fail (58 errors) with status message 'failure while building tuxmake target(s): kernel debugkernel': b65054597872 ("Linux 5.10-rc6") powerpc (tinyconfig) with clang-nightly @ https://builds.tuxbuild.com/1l4Z9RhN8Q521ENnerYGdjpUnHF/
👹 Fail (0 errors) with status message 'failure while building tuxmake target(s): kernel debugkernel': b65054597872 ("Linux 5.10-rc6") mips (tinyconfig) with clang-nightly @ https://builds.tuxbuild.com/1l4Z9RorkzBecrgcjm4Kw80SH6q/
🎉 Pass: b65054597872 ("Linux 5.10-rc6") s390 (tinyconfig) with clang-nightly @ https://builds.tuxbuild.com/1l4Z9RiOFmx5nVrwfGrLEwRmJQV/
👾 Pass (3 warnings): b65054597872 ("Linux 5.10-rc6") arm64 (tinyconfig) with clang-nightly @ https://builds.tuxbuild.com/1l4Z9Q2BEDoPO5ssGjMmHPuTJvU/
```
