from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .kinesis_queue_stream_identifier import KinesisQueueStreamIdentifier


class KinesisQueueSummary(BaseModel):
    QueueName: StrictStr | None = None
    QueueARN: StrictStr | None = None
    QueueStatus: StrictStr | None = None
    QueueCreationTimestamp: datetime.datetime | StrictStr | None = None
    Streams: list[KinesisQueueStreamIdentifier] | None = None
