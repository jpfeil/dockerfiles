FROM ubuntu:14.04

MAINTAINER Jacob Pfeil, jpfeil@ucsc.edu

RUN apt-get update && apt-get install -y wget python-dev python-pip zlib1g-dev 

RUN mkdir /opt/Oncotator/
COPY wrapper.sh /opt/Oncotator/

WORKDIR /home

RUN pip install numpy pyvcf

RUN wget https://github.com/broadinstitute/oncotator/archive/v1.9.0.0.tar.gz -O oncotator-1.9.0.0.tar.gz; \
    tar xvf oncotator-1.9.0.0.tar.gz; cd oncotator-1.9.0.0; pip install .; 

RUN mkdir /data
WORKDIR /data

ENTRYPOINT ["sh", "/opt/Oncotator/wrapper.sh"]
