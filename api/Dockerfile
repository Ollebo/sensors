from ubuntu:18.04

#Run in normal
RUN apt clean 
RUN apt-get update 
RUN apt-get install python3-pip -y
RUN apt-get install python3-flask python3-redis -y


WORKDIR /opt
COPY . /opt/code


#RUN wget http://www.airspayce.com/mikem/bcm2835/bcm2835-1.60.tar.gz
#RUN tar zxvf bcm2835-1.60.tar.gz
#WORKDIR /opt/bcm2835-1.60
#RUN ./configure
#RUN make
#RUN make check
#RUN make install



WORKDIR /opt/code
CMD run.sh