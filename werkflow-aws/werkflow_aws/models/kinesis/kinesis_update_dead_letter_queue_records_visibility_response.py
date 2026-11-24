from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .kinesis_update_dead_letter_queue_records_visibility_error_entry import KinesisUpdateDeadLetterQueueRecordsVisibilityErrorEntry
from .kinesis_update_dead_letter_queue_records_visibility_result_entry import KinesisUpdateDeadLetterQueueRecordsVisibilityResultEntry


class KinesisUpdateDeadLetterQueueRecordsVisibilityResponse(BaseModel):
    Successful: list[KinesisUpdateDeadLetterQueueRecordsVisibilityResultEntry] | None = None
    Failed: list[KinesisUpdateDeadLetterQueueRecordsVisibilityErrorEntry] | None = None
    ResponseMetadata: dict[str, Any] | None = None
