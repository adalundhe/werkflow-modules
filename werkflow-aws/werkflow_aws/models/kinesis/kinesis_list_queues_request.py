from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .kinesis_queue_stream_filter import KinesisQueueStreamFilter


class KinesisListQueuesRequest(BaseModel):
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
    StreamFilter: list[KinesisQueueStreamFilter] | None = None
