from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .kinesis_restore_dead_letter_queue_records_error_entry import KinesisRestoreDeadLetterQueueRecordsErrorEntry
from .kinesis_restore_dead_letter_queue_records_result_entry import KinesisRestoreDeadLetterQueueRecordsResultEntry


class KinesisRestoreDeadLetterQueueRecordsResponse(BaseModel):
    Successful: list[KinesisRestoreDeadLetterQueueRecordsResultEntry] | None = None
    Failed: list[KinesisRestoreDeadLetterQueueRecordsErrorEntry] | None = None
    ResponseMetadata: dict[str, Any] | None = None
