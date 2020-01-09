FROM ubuntu:18.04
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends python3 python3-dev python3-pip python-pip \
    gcc git wget g++ build-essential python3-setuptools \
    libxerces-c-dev qt4-dev-tools freeglut3-dev libmotif-dev tk-dev \
    cmake libxpm-dev libxmu-dev libxi-dev libtinfo5 vim git dpkg-dev cmake g++ gcc binutils libx11-dev libxpm-dev \
    libxft-dev libxext-dev gfortran libssl-dev libpcre3-dev \
    xlibmesa-glu-dev libglew1.5-dev libftgl-dev \
    libmysqlclient-dev libfftw3-dev libcfitsio-dev \
    graphviz-dev libavahi-compat-libdnssd-dev \
    libldap2-dev python-dev libxml2-dev libkrb5-dev \
    libgsl0-dev libqt4-dev && \
    pip3 install wheel && \
    pip3 install numpy && \
    pip install numpy
RUN wget https://root.cern/download/root_v6.18.04.Linux-ubuntu18-x86_64-gcc7.4.tar.gz
RUN tar -xvf root_v6.18.04.Linux-ubuntu18-x86_64-gcc7.4.tar.gz
RUN /bin/bash -c "source /root/bin/thisroot.sh"
RUN echo "source /root/bin/thisroot.sh" >> /root/.bashrc
RUN mkdir geant4
RUN wget http://geant4.cern.ch/support/source/geant4.10.04.p01.tar.gz
RUN mv geant4.10.04.p01.tar.gz geant4
RUN cd geant4 && tar -zxvf geant4.10.04.p01.tar.gz && mkdir build && cd build && \
    /bin/bash -c "cmake -DCMAKE_INSTALL_PREFIX=/geant4/geant4.10.04-install -DGEANT4_INSTALL_DATA=ON /geant4/geant4.10.04.p01; make -j12; make install"
#ENV Geant4_DIR /geant4/build/
RUN git clone https://USER:PASS@gitlab.cern.ch/spacal-rd/spacal-simulation.git && \
    cd spacal-simulation/ && \
    git checkout marco_studies && \
    mkdir build && cd build && \
    /bin/bash -c "source /root/bin/thisroot.sh; export Geant4_DIR=/geant4/build/; cmake ../; make -j12"
RUN echo "source /geant4/geant4.10.04-install/bin/geant4.sh" >> /root/.bashrc


