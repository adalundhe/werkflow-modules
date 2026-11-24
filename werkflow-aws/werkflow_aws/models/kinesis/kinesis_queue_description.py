from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .kinesis_queue_attributes import KinesisQueueAttributes
from .kinesis_queue_stream_configuration import KinesisQueueStreamConfiguration


class KinesisQueueDescription(BaseModel):
    QueueName: StrictStr | None = None
    QueueARN: StrictStr | None = None
    QueueStatus: StrictStr | None = None
    QueueCreationTimestamp: datetime.datetime | StrictStr | None = None
    StreamConfigurationList: list[KinesisQueueStreamConfiguration] | None = None
    QueueAttributes: KinesisQueueAttributes | None = None
