from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .kinesis_queue_record import KinesisQueueRecord


class KinesisReceiveQueueRecordsResponse(BaseModel):
    QueueRecords: list[KinesisQueueRecord] | None = None
    ResponseMetadata: dict[str, Any] | None = None
