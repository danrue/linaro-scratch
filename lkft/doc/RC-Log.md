# Linux Stable Release Candidate Testing Log

Log of status and events while doing release candidate testing in Linaro's
Linux Kernel Functional Test (LKFT) project.

## 2018-01-06
### 4.14.12
Results in <24h.
- Build failure with x15, requiring manual intervention.

## 2018-01-05
### 4.4.110
Results in <24h.
- LTP poll02 failure on x15. Not reproducible. Not considered a regression.
  ([link](https://bugs.linaro.org/show_bug.cgi?id=3566))
### 4.9.75
Results in <24h.
- Build failure with x15, requiring manual intervention.

## 2018-01-01
### 4.4.109
Results in <8h.
### 4.9.74
Results in <8h.
### 4.14.11
Results in <8h.
- kselftest ldt_gdt_64 failure on x86, due to mismatch between kselftest
  version and kernel version.
  ([link](https://bugs.linaro.org/show_bug.cgi?id=3564))
