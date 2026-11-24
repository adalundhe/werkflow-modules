from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BatchGetJobQueueSnapshotRequest(BaseModel):
    jobQueue: StrictStr
