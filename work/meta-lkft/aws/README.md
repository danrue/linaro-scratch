# Experimental AWS builder for LKFT

This experiment uses dynamically provisioned spot ec2 instances for builders
and EFS for build caching.

c5.2xlarge
- 8 vCPU
- 16GB memory
- reserved cost: $.34/hr
- spot cost: ~$.13/hr (+/- .02)

## EFS

EFS cost is $.30/GB/month. It is estimated that LKFT will use approximately
100GB typically.

## Setup

- Create an EFS volume
- Create an ec2 instance.
- Add `user-data` (see local file) to instance
- Ensure instance is in the same VPC, subnet, and sg as EFS
- 

### Build

- Building most of LKFT from scratch used about 15GB on disk
- Initial build took several hours
- Subsequent rebuild of same sources took

EFS space used, for one full build:

```
ubuntu@ip-172-31-65-68:~$ du -hsx /oe/*
6.5G	/oe/downloads
5.1G	/oe/sstate-cache
```

