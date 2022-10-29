From ubuntu:22.04

RUN apt-get update && apt-get install python3-pip python3-pil python3-smbus python3-dev python3-gpiozero -y
RUN pip install RPi.GPIO
RUN pip install spidev
RUN pip install pika
RUN pip3 install requests 

RUN mkdir /ollebo
COPY code/ /ollebo/code/
WORKDIR /ollebo/code


CMD python3 sendToApi.py
