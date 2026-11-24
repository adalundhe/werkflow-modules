from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .kinesis_update_queue_records_visibility_request_entry import KinesisUpdateQueueRecordsVisibilityRequestEntry


class KinesisUpdateQueueRecordsVisibilityRequest(BaseModel):
    QueueARN: StrictStr
    Entries: list[KinesisUpdateQueueRecordsVisibilityRequestEntry]
