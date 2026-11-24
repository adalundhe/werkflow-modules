from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .kinesis_queue_summary import KinesisQueueSummary


class KinesisListQueuesResponse(BaseModel):
    QueueSummaries: list[KinesisQueueSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
