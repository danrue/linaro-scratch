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

Caveat: This does not include the time it takes to publish the build. It's just
the build time. It does however include the time it takes to install docker and
download the docker image - steps which could be baked into the image.

- Building most of LKFT from scratch used about 15GB on disk
- Initial build took several hours

EFS space used, for one full build:

```
ubuntu@ip-172-31-65-68:~$ du -hsx /oe/*
6.5G	/oe/downloads
5.1G	/oe/sstate-cache
```

- no-op rebuild time and cost:
  - c5.2xlarge
  - time: 445 seconds, or .125 of an hour
  - costs:
    - ec2: 1.7 cents
    - ebs: 1.3 cents

- build a new kernel, different branch
  - c5.2xlarge
  - time
  - costs:
