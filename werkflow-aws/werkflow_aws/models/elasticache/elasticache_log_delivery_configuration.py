from pydantic import BaseModel, StrictStr
from typing import Literal
from .elasticache_destination_details import ElasticacheDestinationDetails


class ElasticacheLogDeliveryConfiguration(BaseModel):
    LogType: Literal['slow-log', 'engine-log']
    DestinationType: Literal['cloudwatch-logs', 'kinesis-firehose']
    DestinationDetails: ElasticacheDestinationDetails
    LogFormat: Literal['text', 'json']
    Status: Literal[
        'active',
        'enabling',
        'modifying',
        'disabling',
        'error',
    ] | None = None
    Message: StrictStr | None = None