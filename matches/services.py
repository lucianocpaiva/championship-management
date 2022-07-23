from championship_management import channel
import json


def send_match_event(match_id, events):
    """
    Send events to message queue
    """
    # Create message queue
    channel.queue_declare(queue='events')

    channel.basic_publish(exchange='',
                          routing_key='events',
                          body=json.dumps({'match_id': match_id, 'events': events}))

    print(" [x] Sent %r" % events)

    return True
