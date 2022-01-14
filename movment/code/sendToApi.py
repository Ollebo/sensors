
import pika, sys, os
import requests
import json

url = os.environ.get("URL", 'https://iot.home.ollebo.com/data/')
key = os.environ.get("API_KEY", '1234')

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
    credentials = pika.PlainCredentials('ollebo', 'olle2Pass')
    parameters = pika.ConnectionParameters('rabbitmq',
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