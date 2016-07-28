FROM ubuntu:14.04

MAINTAINER Jacob Pfeil, jpfeil@ucsc.edu

RUN apt-get update && apt-get install -y wget r-base build-essential zlib1g-dev git samtools

RUN mkdir /opt/ericscript/
COPY wrapper.sh /opt/ericscript/

WORKDIR /home

RUN mkdir /home/bin 
ENV PATH /home/bin:$PATH

# Install R
RUN wget -O /tmp/ada_2.0-3.tar.gz https://cran.r-project.org/src/contrib/ada_2.0-5.tar.gz; \
    R CMD INSTALL /tmp/ada_2.0-3.tar.gz

# Install BWA
RUN git clone https://github.com/lh3/bwa.git; cd bwa; make; ln -s /home/bwa/bwa /home/bin/

# Install seqtk
RUN git clone https://github.com/lh3/seqtk.git; cd seqtk; make; ln -s /home/seqtk/seqtk /home/bin/

# Install bedtools
RUN wget https://github.com/arq5x/bedtools2/releases/download/v2.26.0/bedtools-2.26.0.tar.gz; \
    tar xvfz bedtools-2.26.0.tar.gz; cd bedtools2; make; ln -s /home/bedtools2/bin/bedtools /home/bin/

# Install BLAT
RUN wget -P /home/bin/ http://hgdownload.soe.ucsc.edu/admin/exe/linux.x86_64.v287/blat/blat; \
    chmod +x /home/bin/blat

# Install ericscript
RUN wget http://downloads.sourceforge.net/project/ericscript/ericscript-0.5.5.tar.bz2; \
    tar -xjf ericscript-0.5.5.tar.bz2 && chmod +x ericscript-0.5.5/ericscript.pl

RUN mkdir /data
WORKDIR /data

ENTRYPOINT ["sh", "/opt/ericscript/wrapper.sh"]
