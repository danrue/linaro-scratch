# Usage

```
sh test_10.sh
cat test_10.jobs | ./aggregate_jobs.py
```

```
sh test_100.sh
cat test_100.jobs | ./aggregate_jobs.py
```

### 2019-11-06

Submitted 110 jobs in total.

```
$ cat test_10.jobs test_100.jobs | ./aggregate_jobs.py
...
pass rate: 91.82%
pass: 101, fail: 9
1.82% of jobs failed for reason: Name or service not known
3.64% of jobs failed for reason: bootloader-interrupt timed out
1.82% of jobs failed for reason: pdukci --reboot ls2088ardb failed
0.91% of jobs failed for reason: Unable to fetch git repository 'https://github.com
durations of successful jobs:
    min: 640s
    max: 762s
    mean: 664s
    median: 650s
    standard deviation: 27s
```
