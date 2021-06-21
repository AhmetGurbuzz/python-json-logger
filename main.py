import json
import logging
from time import time


class JsonFormatter(logging.Formatter):
    def __init__(self):
        super().__init__()

    def format(self, record):
        if isinstance(record, str):
            return record.msg
        else:
            return record.msg.__str__()


class Json:
    def __init__(self,
                 msg,
                 timestamp=str(int(time())),
                 payload=None):
        self.msg = msg
        self.payload = payload
        self.timestamp = timestamp

    def __str__(self):
        return json.dumps(self.__dict__)


if __name__ == '__main__':
    logger = logging.getLogger(f'{__name__}')
    logging.basicConfig(
        format='[%(levelname)s] [%(pathname)s] [%(asctime)s] [%(name)s] %(message)s',
        level=logging.INFO,
        datefmt='%d/%m/%Y %I:%M:%S %p'
    )

    ch = logging.StreamHandler()
    ch.setFormatter(JsonFormatter()), ch.setLevel(logging.INFO)
    logger.addHandler(ch)

    logger.info(Json(msg='message', payload={'key': 'value', '_key': '_value'}))

