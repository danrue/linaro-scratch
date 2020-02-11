#!/bin/bash

set -x
set -e

SERVER="https://snapshots.linaro.org"
PATHS="openembedded/lkft/lkft/sumo/am57xx-evm/lkft/linux-stable-rc-5.5/9/ openembedded/lkft/lkft/sumo/dragonboard-410c/lkft/linux-stable-rc-5.5/9/ openembedded/lkft/lkft/sumo/hikey/lkft/linux-stable-rc-5.5/9/ openembedded/lkft/lkft/sumo/intel-core2-32/lkft/linux-stable-rc-5.5/9/ openembedded/lkft/lkft/sumo/intel-corei7-64/lkft/linux-stable-rc-5.5/9/ openembedded/lkft/lkft/sumo/juno/lkft/linux-stable-rc-5.5/9/ openembedded/lkft/lkft/sumo/ls2088ardb/lkft/linux-stable-rc-5.5/9/"
#PATHS="openembedded/lkft/lkft/sumo/am57xx-evm/lkft/linux-stable-rc-5.5/9/ openembedded/lkft/lkft/sumo/dragonboard-410c/lkft/linux-stable-rc-5.5/9/"
DESTINATION="s3://storage.lkft.org/snapshots"
SCRATCH=scratch

for path in $PATHS; do
    for file in $(curl -s -L $SERVER/api/ls/$path | jq -r ".files[].url"); do
        if [ -f $SCRATCH$file ]; then
            continue
        fi
        if echo "$file" | grep -q '/$'; then
            # XXX Directories not supported
            # Add the paths to PATHS above to get them copied.
            echo "skipping directory $file"
            continue
        fi
        mkdir -p $SCRATCH$(dirname $file)
        echo "Downloading $SERVER$file to $SCRATCH$file"
        curl -L -s -o $SCRATCH$file $SERVER$file
    done
done

for md5file in $(find $SCRATCH -name MD5SUMS.txt); do
    dir=$(dirname $md5file)
    file=$(basename $md5file)
    echo "Checking checksums in $dir"
    pushd $dir
    md5sum --ignore-missing --check $file
    popd
done
#for shafile in $(find $SCRATCH -name SHA256SUMS.txt); do
#    dir=$(dirname $shafile)
#    file=$(basename $shafile)
#    echo "Checking checksums in $dir"
#    cd $dir
#    for line in $(cat $file); do
#        sha256sum --ignore-missing --check $file || true
#    done
#    cd ..
#done

aws s3 sync $SCRATCH/ $DESTINATION/
