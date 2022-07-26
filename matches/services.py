from championship_management import channel
import json

import logging
logger = logging.getLogger(__name__)


def send_match_event(events):
    """
    Send events to message queue
    """

    if not channel:
        logger.info('Message queue is not active')
        return
    
    # Create exchange
    channel.exchange_declare(exchange= 'events', exchange_type='fanout')
    
    result = channel.queue_declare(queue='consumer01')
    queue_name = result.method.queue

    channel.queue_bind(exchange='events', queue=queue_name)

    channel.basic_publish(exchange='events',
                          routing_key='',
                          body=json.dumps(events))

    print(" [x] Sent %r" % events)

    return True
