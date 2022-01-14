
import pika, sys, os
import requests
import json
import time
import socket

url = os.environ.get("URL", 'https://iot.home.ollebo.com/data/')
key = os.environ.get("API_KEY", '1234')
rabbithost = os.environ.get("RABBITMQ", 'rabbitmq')
rabbituser = os.environ.get("RABBITMQ_USER", 'ollebo')
rabbitpass = os.environ.get("RABBITMQ_USER", 'olle2Pass')




def wait_for_port(port, host='localhost', timeout=5.0):
    """Wait until a port starts accepting TCP connections.
    Args:
        port (int): Port number.
        host (str): Host address on which the port should exist.
        timeout (float): In seconds. How long to wait before raising errors.
    Raises:
        TimeoutError: The port isn't accepting connection after time specified in `timeout`.
    """
    start_time = time.perf_counter()
    while True:
        try:
            with socket.create_connection((host, port), timeout=timeout):
                break
        except OSError as ex:
            print("No connection to {0} on port {1}".format(host,port))
            time.sleep(1)
            if time.perf_counter() - start_time >= timeout:
                raise TimeoutError('Waited too long for the port {} on host {} to start accepting '
                                   'connections.'.format(port, host)) from ex






def sendData(data):
    '''
    Send the data to the endpint
    '''
    print(data)
    decodeData= data.decode('utf-8')
    print(decodeData)
    JSONdata = decodeData.replace('\'','"')
    print(JSONdata)
    r = requests.post(url, data=JSONdata, headers={'X-Api-Key': '1234','Content-type': 'application/json'})
    r.status_code
    if r.status_code == 200:
        print("Data accepted by API")
    else:
        print("Error sending data")
        print(r.status_code)




def main():
    
    wait_for_port(5672, host=rabbithost, timeout=30.0)


    credentials = pika.PlainCredentials(rabbituser, rabbitpass)
    parameters = pika.ConnectionParameters(rabbithost,
                                       5672,
                                       '/',
                                       credentials)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    channel.queue_declare(queue='mesurement')

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)
        sendData(body)

    channel.basic_consume(queue='mesurement', on_message_callback=callback, auto_ack=True )

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)