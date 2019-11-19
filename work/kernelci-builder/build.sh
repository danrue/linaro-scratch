- ./kci_build build_kernel --build-env ${build_env} --kdir $CI_PROJECT_DIR --arch ${arch} --defconfig defconfig --output $KCI_OUTPUT #--verbose
- ./kci_build install_kernel --kdir $CI_PROJECT_DIR  --tree-name $TREE_NAME --tree-url $CI_PROJECT_URL --branch $CI_COMMIT_REF_NAME --output $KCI_OUTPUT
- ./kci_build push_kernel --kdir=$CI_PROJECT_DIR --token=$KCI_TOKEN --api=$KCI_API
- ./kci_build publish_kernel --kdir=$CI_PROJECT_DIR --token=$KCI_TOKEN --api=$KCI_API

PYTHONPATH=/path/to/kernelci-core/kernelci /path/to/kernelci-core/kci_build --yaml-configs=/path/to/kernelci-core/build-configs.yaml list_configs

drue@xps:~/src/linux/mainline$ PYTHONPATH=/home/drue/src/kernelci/kernelci-core/kernelci python2 /home/drue/src/kernelci/kernelci-core/kci_build --yaml-configs /home/drue/src/kernelci/kernelci-core/build-configs.yaml list_configs





drue@xps:~/src/linux/mainline$ PYTHONPATH=/home/drue/src/kernelci/kernelci-core/kernelci python2 /home/drue/src/kernelci/kernelci-core/kci_build build_kernel --build-env gcc-8 --kdir /home/drue/src/linux/mainline --arch x86 --defconfig defconfig --output /home/drue/src/linux/mainline/build-x86-gcc-8
drue@xps:~/src/kernelci/kernelci-core$ python2 kci_build install_kernel --kdir /home/drue/src/linux/mainline --output /home/drue/src/linux/mainline/build-x86-gcc-8 --tree-url bar --branch baz --tree-name foo


