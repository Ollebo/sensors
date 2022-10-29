from balenalib/raspberry-pi

ENV LD_LIBRARY_PATH=/opt/vc/lib/

RUN apt-get update && apt-get install python3-pip python3-pil python3-smbus python3-dev python3-gpiozero -y
RUN pip3 install picamera 
RUN pip3 install gpsphoto
RUN pip3 install exifread
RUN pip3 install piexif

RUN mkdir /ollebo
COPY code/ /ollebo/code/
WORKDIR /ollebo/code


CMD python3 snap.py