from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .kinesis_queue_attributes import KinesisQueueAttributes


class KinesisUpdateQueueRequest(BaseModel):
    QueueARN: StrictStr
    QueueAttributes: KinesisQueueAttributes
