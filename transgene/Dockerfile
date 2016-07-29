FROM ubuntu:14.04

MAINTAINER Jacob Pfeil, jpfeil@ucsc.edu

RUN apt-get update && apt-get install -y git

RUN mkdir /opt/transgene/
COPY wrapper.sh /opt/transgene/

WORKDIR /home

RUN git clone https://github.com/jpfeil/Transgene.git; \
    git checkout issues/1-add-fusion-support; ln -s /home/Transgene/transgene.py /home/bin; \
    chmod +x /home/bin/transgene.py

RUN mkdir /home/bin 
ENV PATH /home/bin:$PATH

ENTRYPOINT ["sh", "/opt/transgene/wrapper.sh"]
