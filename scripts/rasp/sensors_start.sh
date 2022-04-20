### BEGIN INIT INFO
# Provides:          sensors_start.sh
# Required-Start:    $remote_fs $syslog
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Start daemon at boot time
# Description:       Enable service provided by daemon.
### END INIT INFO

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