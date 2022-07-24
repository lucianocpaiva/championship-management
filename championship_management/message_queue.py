from django.conf import settings
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host=settings.RABBITMQ['HOST'], credentials=pika.PlainCredentials(settings.RABBITMQ['USER'], settings.RABBITMQ['PASSWORD'])))

channel = connection.channel()
