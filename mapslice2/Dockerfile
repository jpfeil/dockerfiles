FROM ubuntu:14.04

MAINTAINER Jacob Pfeil, jpfeil@ucsc.edu

RUN apt-get update && apt-get install -y wget python-dev unzip make build-essential zlib1g-dev \
    libncurses5-dev libncursesw5-dev

RUN mkdir /opt/mapsplice2/
COPY wrapper.sh /opt/mapsplice2/

WORKDIR /home

RUN wget http://protocols.netlab.uky.edu/~zeng/MapSplice-v2.1.8.zip;\
    unzip MapSplice-v2.1.8.zip; cd MapSplice-v2.1.8; make; \
    chmod +x mapsplice.py;

RUN mkdir /data
WORKDIR /data

ENTRYPOINT ["sh", "/opt/mapsplice2/wrapper.sh"]
