# Linux Stable Release Candidate Testing Log

Log of status and events while doing release candidate testing in Linaro's
Linux Kernel Functional Test (LKFT) project.

## 2018-03-02
- git.yoctoproject.org outage caused build delays in 4.4 and 4.14
- db410c and qemu x86_64 reported for first time
### 4.4.120
Results in <24h
### 4.9.86
Results in <24h
### 4.14.24
Results in <24h

## 2018-02-26
- Builds took ~2h. Needed to rebuild 4.9/hikey for 'sstate_create_package' failure.
### 4.4.119
Results in <24h
### 4.9.85
Results in <24h
### 4.14.23
Results in <24h
### 4.15.7
Results in <24h

## 2018-02-23
- All builds worked first time
- Limited availability (Friday evening push (UTC))
  - multiple pushes
### 4.4.118
- Results in <8h
### 4.9.84
- Results in <48h
### 4.14.22
- Results in <8h
### 4.15.6
- Results in <48h

## 2018-02-21
- Issue with lkft.v.l.o being slow. Squad had issues submitting jobs and
  fetching results.
### 4.4.117
- Results in <8h
### 4.9.83
- Results in <8h
- arm64 legitimate build failure, reported, patch dropped
### 4.14.21
- Results in <8h
### 4.15.5
- Results in <8h
- build failure on x15 "Function failed: sstate_create_package"

## 2018-02-15
- Builds took 7 hours. 13 total failures.
  - Some hikey failures caused by breakage introduced same day
  - Others caused by long standing git-related issues in jenkins environment
    - Fixed (hopefully permanently) with 'bitbake -c cleanall edk2-hikey'
### 4.4.116
Results in <24h
### 4.9.82
Results in <24h
- Noted getrusage04 intermittent failure
  https://bugs.linaro.org/show_bug.cgi?id=3507
### 4.14.20
Results in <24h
### 4.15.4
Results in <24h
- Noted netns_netlink failure on x15. See https://bugs.linaro.org/show_bug.cgi?id=3484

## 2018-02-09
- LTP was upgraded from 20170929 to 20180118, causing a falsely reported
  regression in fanotify06.
### 4.9.81
Results in <8h
### 4.14.19
Results in <8h
### 4.15.3
Results in <8h

## 2018-02-05
### 4.14.18
Results in <8h
### 4.15.2
Results in <8h

## 2018-02-02
### 4.4.115
Results in <8h
### 4.9.80
Results in <8h
### 4.14.17
Results in <8h
### 4.15.1
Results in <24h
- This was the first 4.15 RC.
- Report showed false failures because the new branch was not yet baselined,
  and also because we were running 4.14 kselftest against 4.15.
- 4.15 build was submitted for review but not yet merged when the branch was
  released, causing last minute Friday afternoon scramble (thanks Daniel).
  Should have had it building and baselined ahead of time.

## 2018-01-29
### 4.4.114
Results in <24h
### 4.9.79
Results in <24h
### 4.14.16
Results in <24h

## 2018-01-22
### 4.4.113
Results in <24h
- Issue with 'main.sh' kselftest on hikey due to missing patch on linaro's
  hikey tree. Resolved.
### 4.9.78
Results in <24h
### 4.14.15
Results in <24h

## 2018-01-15
- Greg requested verifying bpf in 4.4 and 4.9 but we did not have a good way to
  do so. Tests aren’t backported. We are looking at getting bcc running on
  hikey, as a means of manual verification.
### 4.4.112
Results in <24h
- Build (infrastructure) failure with hikey, requiring manual intervention.
- 5 RCs
### 4.9.77
Results in <24h
- 6 RCs
### 4.14.14
Results in <24h
- Build (infrastructure) failure with hikey, requiring manual intervention.
- 4 RCs

## 2018-01-08
### 4.4.111
Results in <24h
- Release candidate republished 4 times
### 4.9.76
Results in <24h
- Release candidate republished 5 times
### 4.14.13
Results in <24h
- Release candidate republished 3 times

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
