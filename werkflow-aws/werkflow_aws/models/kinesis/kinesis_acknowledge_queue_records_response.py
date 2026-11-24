from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .kinesis_acknowledge_queue_records_error_entry import KinesisAcknowledgeQueueRecordsErrorEntry
from .kinesis_acknowledge_queue_records_result_entry import KinesisAcknowledgeQueueRecordsResultEntry


class KinesisAcknowledgeQueueRecordsResponse(BaseModel):
    Successful: list[KinesisAcknowledgeQueueRecordsResultEntry] | None = None
    Failed: list[KinesisAcknowledgeQueueRecordsErrorEntry] | None = None
    ResponseMetadata: dict[str, Any] | None = None
