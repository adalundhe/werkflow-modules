from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .kinesis_restore_dead_letter_queue_records_request_entry import KinesisRestoreDeadLetterQueueRecordsRequestEntry


class KinesisRestoreDeadLetterQueueRecordsRequest(BaseModel):
    QueueARN: StrictStr
    Entries: list[KinesisRestoreDeadLetterQueueRecordsRequestEntry]
