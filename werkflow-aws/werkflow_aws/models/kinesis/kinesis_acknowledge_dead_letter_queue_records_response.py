from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .kinesis_acknowledge_dead_letter_queue_records_error_entry import KinesisAcknowledgeDeadLetterQueueRecordsErrorEntry
from .kinesis_acknowledge_dead_letter_queue_records_result_entry import KinesisAcknowledgeDeadLetterQueueRecordsResultEntry


class KinesisAcknowledgeDeadLetterQueueRecordsResponse(BaseModel):
    Successful: list[KinesisAcknowledgeDeadLetterQueueRecordsResultEntry] | None = None
    Failed: list[KinesisAcknowledgeDeadLetterQueueRecordsErrorEntry] | None = None
    ResponseMetadata: dict[str, Any] | None = None
