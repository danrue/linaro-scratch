docker run -t -e DISTRO=lkft -e MACHINE=intel-corei7-64 -e KERNEL_RECIPE=linux-generic-stable-rc -e KERNEL_VERSION=4.19 -e SRCREV_kernel=178574b66509c9ff7df4ad26c84a8884567e93b4 -v /oe/downloads:/oe/downloads -v /oe/sstate-cache:/oe/sstate-cache -v $(pwd)../build-intel-corei7-64:/oe/build-lkft mrchapp/lkft-rocko bitbake rpb-console-image-lkft    