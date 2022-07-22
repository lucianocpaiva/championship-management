import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq', credentials=pika.PlainCredentials('admin', 'admin')))
channel = connection.channel()
