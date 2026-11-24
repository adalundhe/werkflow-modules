from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .kinesis_queue_description import KinesisQueueDescription


class KinesisCreateQueueResponse(BaseModel):
    QueueDescription: KinesisQueueDescription | None = None
    ResponseMetadata: dict[str, Any] | None = None
