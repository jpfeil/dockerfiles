FROM ubuntu:14.04

MAINTAINER Jacob Pfeil, jpfeil@ucsc.edu

RUN apt-get update && apt-get install -y wget python-dev python-numpy \
    zlib1g-dev libncurses-dev

RUN mkdir /opt/pyPrada/
COPY wrapper.sh /opt/pyPrada/

WORKDIR /home

RUN wget http://downloads.sourceforge.net/project/prada/pyPRADA/pyPRADA_1.2.tar.gz; tar xvf pyPRADA_1.2.tar.gz

ENV PATH /home/pyPRADA_1.2:$PATH

# Install pysam
RUN wget https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/pysam/pysam-0.6.tar.gz; \
    tar xvf pysam-0.6.tar.gz; cd pysam-0.6; python setup.py install

RUN wget http://biopython.org/DIST/biopython-1.60.tar.gz; tar zxfv biopython-1.60.tar.gz; \
    cd biopython-1.60; python setup.py install

RUN mkdir /data
WORKDIR /data

ENTRYPOINT ["sh", "/opt/pyPrada/wrapper.sh"]
