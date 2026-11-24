from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BatchDescribeServiceJobRequest(BaseModel):
    jobId: StrictStr
