from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .kinesis_update_queue_records_visibility_error_entry import KinesisUpdateQueueRecordsVisibilityErrorEntry
from .kinesis_update_queue_records_visibility_result_entry import KinesisUpdateQueueRecordsVisibilityResultEntry


class KinesisUpdateQueueRecordsVisibilityResponse(BaseModel):
    Successful: list[KinesisUpdateQueueRecordsVisibilityResultEntry] | None = None
    Failed: list[KinesisUpdateQueueRecordsVisibilityErrorEntry] | None = None
    ResponseMetadata: dict[str, Any] | None = None
