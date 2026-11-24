from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .batch_job_queue_detail import BatchJobQueueDetail


class BatchDescribeJobQueuesResponse(BaseModel):
    jobQueues: list[BatchJobQueueDetail] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
