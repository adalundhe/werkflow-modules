from pydantic import BaseModel, StrictStr
from typing import Literal
from .destination_details import DestinationDetails


class LogDeliveryConfiguration(BaseModel):
    LogType: Literal['slow-log', 'engine-log']
    DestinationType: Literal['cloudwatch-logs', 'kinesis-firehose']
    DestinationDetails: DestinationDetails
    LogFormat: Literal['text', 'json']
    Status: Literal[
        'active',
        'enabling',
        'modifying',
        'disabling',
        'error',
    ] | None = None
    Message: StrictStr | None = None