#!/bin/bash

echo "Lets startup the stream service"
cd /home/pi/stream
docker-compose start

sleep 30


echo "Lets startup the sensors"
cd /home/pi/ollebo/sensors
docker-compose start


#run for 10h
sleep 6000



echo "Lets stop the sensors"
cd /home/pi/ollebo/sensors
docker-compose stop



sleep 30
echo "Lets startup the stream service"
cd /home/pi/stream
docker-compose stop