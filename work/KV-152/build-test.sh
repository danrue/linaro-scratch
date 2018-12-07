#!/bin/sh
set -ex
for branch in mainline 4.4 4.9 4.14 4.19; do
    for arch in arm arm64 x86_64 i386; do
        if [ $arch = 'arm' ]; then
            defconfig="arch/arm/configs/multi_v7_defconfig"
            crosscompile="arm-linux-gnueabihf-"
        elif [ $arch = 'arm64' ]; then
            defconfig="arch/arm64/configs/defconfig"
            crosscompile="aarch64-linux-gnu-"
        elif [ $arch = 'x86_64' ]; then
            defconfig="arch/x86/configs/x86_64_defconfig"
            crosscompile=""
        elif [ $arch = 'i386' ]; then
            defconfig="arch/x86/configs/i386_defconfig"
            crosscompile=""
        else
            echo "ERROR!"
            exit 1
        fi
        if [ -e .$branch.$arch.built ]; then
            echo "$branch $arch already built; continuing"
            continue
        fi
        (cd linux/$branch &&
            ARCH=$arch CROSSCOMPILE=$crosscompile ./scripts/kconfig/merge_config.sh $defconfig ../../lkft-fragments/$arch.frag &&
            make ARCH=$arch CROSS_COMPILE=$crosscompile -j12
        )
        touch .$branch.$arch.built
    done
done
