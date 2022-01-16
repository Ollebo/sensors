# Sensoring
Sensor stack to read sensor data from Raspberry Pi Sensor hat.
And send data to vstech.se monitoring.


### Req
#### Sensor
I sensor hat mounted on the raspberry pi 

https://www.waveshare.com/product/raspberry-pi/hats/sense-hat-b.htm?___SID=U

#### K3s 
A k3s cluster running on the raspberry pi
https://k3s.io/


#### vstech.se
A vstech account to recive data and to display.



### Install

#### make the raspberry ready
Ro run the stack both docker and k3s need to be installed. Follow the guide on k3s.io to install k3s.

First setup rastberry to handle cgroups

add the following to /boot/cmdline.txt

```
cgroup_memory=1 cgroup_enable=memory
```

It should something like this

```
cat /boot/cmdline.txt 


console=serial0,115200 console=tty1 root=PARTUUID=7790d459-02 rootfstype=ext4 fsck.repair=yes rootwait quiet splash plymouth.ignore-serial-consoles cgroup_memory=1 cgroup_enable=memory
```
Then reboot to make the change take.

Now we are ready to install k3s 

```
curl -sfL https://get.k3s.io | sh -
```

Verfy you have a cluster by running.


```
kubectl get nodes
```


#### Install the sensor stack
Then sensor stack has 3 ore more compenets

1. A rabbitmq que that works as a bridge between the sensors and api

2. A Sensor we can use diffrent sensor they are started and collects data. The data is then added to the rabbitmq que

3. SendToApi this service reads the events from the que and send them to the vstech.se andpoint





First lets setup the rabbitmq
```
kubectl apply -f manifest/rabbitmq.yaml
```


Now lets deploy the sendtoApi  and first we need to add our settings 

Open the file manifest/sendToApi.yaml and edit the values to match your settings.
2 values you need to get from vstech.se. The oter values you can change so that you can find this sensor when searching in grafana.


```
            - name: URL
              value: https://iot.home.ollebo.com/data/   <---get this from vstech.se
            - name: API_KEY
              value: "1234"                             <--- get this from vstech.se
            - name: ID
              value: "1234"
            - name: HOSTNAME
              value: localhost
            - name: CLIENT
              value: k8s
            - name: DEVICE_ID
              value: local
```

Lets deploy the send to api 
```
kubectl apply -f manifest/sendToApi.yaml
```


Verify both pods are upp and running and if they up lets deploy our sensor


```
```
kubectl apply -f manifest/sensor.yaml
```
```
