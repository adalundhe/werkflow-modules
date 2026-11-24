from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .batch_front_of_queue_job_summary import BatchFrontOfQueueJobSummary


class BatchFrontOfQueueDetail(BaseModel):
    jobs: list[BatchFrontOfQueueJobSummary] | None = None
    lastUpdatedAt: StrictInt | None = None
