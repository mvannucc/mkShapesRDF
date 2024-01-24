FROM registry.hub.docker.com/dodasts/root-in-docker:ubuntu22-kernel-v1


WORKDIR /code

USER root



RUN apt-get update && \
    apt-get install -y vim && \
    apt-get install -y voms-clients && \
    apt-get -y install python3.8-venv && \
    echo "deb http://archive.ubuntu.com/ubuntu/ jammy main universe" >> /etc/apt/sources.list.d/xrootd.list && \
    apt-get update && \
    apt-get install -y xrootd-client && \
    apt-get install -y krb5-user && \
    apt-get install -y libkrb5-dev && \
    apt-get install -y libauthen-krb5-perl



COPY ./ /code/

RUN cd /code/ && \
    ./install.sh && \
    mkdir xrdfs_locallib && \
    cd xrdfs_locallib && \
    rsync -ar --exclude 'python3.9' --exclude 'libROO*' --exclude 'libRoo*' /cvmfs/sft.cern.ch/lcg/views/LCG_103/x86_64-ubuntu2004-gcc9-opt/lib ./ && \
    cd .. 
    



