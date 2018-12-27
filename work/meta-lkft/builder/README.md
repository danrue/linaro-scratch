# Experimental AWS builder for LKFT

This experiment uses dynamically provisioned EC2 spot instances for builders,
EFS for build caching, and S3 for artifact storage.

The instance type in use is a c5.2xlarge:
- 8 vCPU
- 16GB memory
- reserved cost: $.34/hr
- spot cost: ~$.13/hr (+/- .02)

A typical LKFT OE build takes between 10 and 15 minutes. The total cost of a
build is less than $.05, and all builds can happen in parallel.

Example run:
```sh
    $ ./build.py user-data
    Starting build
    Submitting spot instance request
    Spot instance request submitted
    Spot instance request fulfilled (5 seconds)
    Instance i-0f0c377e385faf638 launched
    Waiting until instance is running
    Instance is running (5 seconds)
    Instance is online at 35.170.56.200
    Waiting until instance is terminated
    Instance terminated (606 seconds)
    Build complete (618 seconds)
```

Building 10 separate versions in parallel took an average of 826 seconds - min
of 740s, max of 1124s. See
https://gist.github.com/danrue/6833a024075227b89c3e56c4c7f5e92d for output of a
10-build test.

The build results can be seen at
http://therub-builds.s3-website-us-east-1.amazonaws.com/. Note that this
implementation uses simple S3 interfaces, but it could use linaro-cp instead.

Inside each build is a build_YYYYMMDDHHMMSS directory, which contains the log
files from the server for the build.

## EFS

EFS is used to present the build cache over NFS. EFS cost is $.30/GB/month. It
is estimated that LKFT will use approximately 100GB typically.

A prune job can be added to the regular run to run at some frequency. The
problem is that atime is not available. ctime can be used, but, will cause some
unnecessary re-builds over time. This ends up being a build-time vs
storage-cost trade-off.

## Setup

Before using this, an AWS account needs to have some things set up:
- Create a VPC
- Create an EFS volume
- Ensure instance is in the same VPC, subnet, and sg as EFS

These resources are passes as parameters to the spotBuilder class.
