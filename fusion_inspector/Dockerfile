# ProTECT Dockerfile for STAR-Fusion
#
# Build with: sudo docker build --force-rm --no-cache -t jpfeil/fusion-inspector:protect - < 04_03_03_fusion_inspector_Dockerfile
# Run with sudo docker run -v <IO_folder>:/data jpfeil/fusion-inspector:protect <parameters>

# Use pimmuno
FROM ubuntu:14.04

MAINTAINER Jacob Pfeil, jpfeil@ucsc.edu

RUN apt-get update --fix-missing && \
    apt-get install -y dpkg zlib1g-dev gzip perl libdb-dev build-essential wget make git samtools

 RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" | tee /etc/apt/sources.list.d/webupd8team-java.list && \
     echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" | tee -a /etc/apt/sources.list.d/webupd8team-java.list && \
     apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886 && \
     apt-get update && \
     echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections && \
     apt-get install -y oracle-java8-installer

RUN cpan App::cpanminus && cpanm Set::IntervalTree && cpanm DB_File && cpanm URI

WORKDIR /opt

RUN mkdir /opt/docker_wrappers
COPY wrapper.sh /opt/docker_wrappers

RUN git clone --recursive https://github.com/jpfeil/FusionInspector.git && \
    wget -qO- https://github.com/alexdobin/STAR/archive/2.5.2b.tar.gz | tar xz && \
    wget -qO- wget https://github.com/trinityrnaseq/trinityrnaseq/archive/Trinity-v2.3.2.tar.gz | tar xz && \
    cd trinityrnaseq-Trinity-v2.3.2 && make && cd /opt && \
    wget -qO- wget http://research-pub.gene.com/gmap/src/gmap-gsnap-2016-11-07.tar.gz | tar xz && \
    cd gmap-2016-11-07 && ./configure && make && make check && make install

ENV PATH "/opt/FusionInspector/:/opt/STAR-2.5.2b/bin/Linux_x86_64/:$PATH"

# FusionInspector needs the TRINITY_HOME environment variable
ENV TRINITY_HOME "/opt/trinityrnaseq-Trinity-v2.3.2/"

WORKDIR /data

ENTRYPOINT ["sh", "/opt/docker_wrappers/wrapper.sh"]
CMD ["--help"]
