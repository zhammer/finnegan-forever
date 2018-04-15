"""AWS lambda function delivery for reading the current passage of Finnegan's Wake."""

import json
import logging
import time
import os
from finnegan_forever.gateways.scroll_gateway import ScrollGateway
from finnegan_forever.read_current_passage import read_current_passage

def handler(event, context):
    """AWS lambda event handler for read_finnegan."""
    logger = logging.getLogger(__name__)
    logger.info('Handling event: %s', event)

    finnegan_scroll_filepath = os.environ['FINNEGAN_SCROLL_FILEPATH']
    passage_size = int(os.environ['PASSAGE_SIZE'])
    window_length = int(os.environ['WINDOW_LENGTH'])

    finnegan_scroll = ScrollGateway(finnegan_scroll_filepath)

    try:
        passage = read_current_passage(
            scroll=finnegan_scroll,
            passage_size=passage_size,
            window_length=window_length,
            seconds=int(time.time())
        )
    except Exception as e:
        logger.error('Encountered error while handling event. (event: "%s". error: "%s")', event, e)
        return {'statusCode': 500}

    body = {
        'passage': passage,
        'reading_every': window_length
    }

    return {
        'statusCode': 200,
        'body': json.dumps(body)
    }
