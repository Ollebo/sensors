import pika
import json 
credentials = pika.PlainCredentials('ollebo', 'olle2Pass')
parameters = pika.ConnectionParameters('rabbitmq',
                                   5672,
                                   '/',
                                   credentials)

connection = pika.BlockingConnection(parameters)

channel = connection.channel()

channel.queue_declare(queue='mesurement')




def addToRabbit(routing,data):
    '''
    Adding data to rabbit server
    '''
    channel.basic_publish(exchange='',
                      routing_key=routing,
                      body=str(data))
    print(" [x] Sent to Rabbit {0}".format(routing))
    #connection.close()


addToRabbit('movement','{"data":"1"}')