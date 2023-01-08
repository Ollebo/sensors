from python

ENV LANG=en_US.UTF-8
ENV LC_ALL=en_US.UTF-8
ENV LANGUAGE=en_US:en
ENV TZ=Europe/London
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update && apt-get install python3-dev python3-pip -y
RUN pip3 install --upgrade setuptools  wheel


#Fix req
RUN pip3 install  flask
RUN pip3 install Adafruit_Python_DHT

# Copy files
COPY . /code
RUN chmod +x /code/run.sh


CMD /code/run.sh 
