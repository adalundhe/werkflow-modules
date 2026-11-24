from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .kinesis_acknowledge_queue_records_request_entry import KinesisAcknowledgeQueueRecordsRequestEntry


class KinesisAcknowledgeQueueRecordsRequest(BaseModel):
    QueueARN: StrictStr
    Entries: list[KinesisAcknowledgeQueueRecordsRequestEntry]
