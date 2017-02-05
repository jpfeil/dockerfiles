FROM ubuntu:14.04

MAINTAINER Jacob Pfeil, jpfeil@ucsc.edu

RUN apt-get update && apt-get install -y git python-dev python-pip zlib1g-dev

RUN mkdir /opt/transgene/
COPY wrapper.sh /opt/transgene/

WORKDIR /home

RUN mkdir /home/bin 
ENV PATH /home/bin:$PATH

RUN pip install pysam swalign 

RUN git clone https://github.com/jpfeil/Transgene.git; cd Transgene; \
    git checkout issues/1-add-fusion-support; ln -s /home/Transgene/transgene.py /home/bin/; \
    chmod +x /home/bin/transgene.py

RUN mkdir /data
WORKDIR /data

ENTRYPOINT ["sh", "/opt/transgene/wrapper.sh"]
