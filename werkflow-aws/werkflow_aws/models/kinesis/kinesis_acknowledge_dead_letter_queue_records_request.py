from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .kinesis_acknowledge_dead_letter_queue_records_request_entry import KinesisAcknowledgeDeadLetterQueueRecordsRequestEntry


class KinesisAcknowledgeDeadLetterQueueRecordsRequest(BaseModel):
    QueueARN: StrictStr
    Entries: list[KinesisAcknowledgeDeadLetterQueueRecordsRequestEntry]
