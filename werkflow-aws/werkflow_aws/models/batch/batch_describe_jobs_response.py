from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .batch_job_detail import BatchJobDetail


class BatchDescribeJobsResponse(BaseModel):
    jobs: list[BatchJobDetail] | None = None
    ResponseMetadata: dict[str, Any] | None = None
