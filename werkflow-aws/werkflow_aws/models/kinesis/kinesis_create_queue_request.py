from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .kinesis_queue_attributes import KinesisQueueAttributes
from .kinesis_queue_stream_configuration import KinesisQueueStreamConfiguration


class KinesisCreateQueueRequest(BaseModel):
    QueueName: StrictStr
    StreamConfigurationList: list[KinesisQueueStreamConfiguration]
    QueueAttributes: KinesisQueueAttributes | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
