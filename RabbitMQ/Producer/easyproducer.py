#!/usr/bin/env python
# coding=utf-8
import pika

credentials = pika.PlainCredentials('user', 'user123')
parameters = pika.ConnectionParameters('localhost', 5672, '/', credentials)

connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='hello')

for i in range(10000000):  # тут выбираешь, сколько сообщений слать
    body = f'Hello Netology! #{i}'
    channel.basic_publish(
        exchange='',
        routing_key='hello',
        body=body.encode('utf-8')
    )
    print(f'Отправил: {body}')

connection.close()
