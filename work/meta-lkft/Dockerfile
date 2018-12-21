FROM debian:stretch
MAINTAINER Daniel Díaz <daniel.diaz@linaro.org>

RUN apt-get update \
 && DEBIAN_FRONTEND=noninteractive apt dist-upgrade -y

RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    binutils \
    bzip2 \
    ca-certificates \
    chrpath \
    cpio \
    cpp \
    diffstat \
    file \
    g++ \
    gawk \
    gcc \
    git \
    libc-dev-bin \
    libssl-dev \
    locales \
    make \
    patch \
    python \
    python3 \
    sudo \
    texinfo \
    wget

ENV LC_ALL=en_US.UTF-8
RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen \
 && locale-gen

RUN useradd -m lkftuser
RUN mkdir /oe && chown lkftuser:lkftuser /oe
RUN echo 'lkftuser ALL = NOPASSWD: ALL' > /etc/sudoers.d/lkft \
 && chmod 0440 /etc/sudoers.d/lkft

USER lkftuser
WORKDIR /home/lkftuser/

RUN git config --global user.name "LKFT OE User" \
 && git config --global user.email "lkft-maintainers@lists.linaro.org" \
 && git config --global color.ui auto

RUN mkdir $HOME/lkft $HOME/bin \
 && wget https://storage.googleapis.com/git-repo-downloads/repo -O $HOME/bin/repo \
 && chmod +x $HOME/bin/repo

WORKDIR /oe
RUN $HOME/bin/repo init -b lkft/rocko -u https://github.com/96boards/oe-rpb-manifest \
 && $HOME/bin/repo sync

COPY lkft-bitbake-helper /home/lkftuser/bin/lkft-bitbake-helper

ENTRYPOINT ["/home/lkftuser/bin/lkft-bitbake-helper"]