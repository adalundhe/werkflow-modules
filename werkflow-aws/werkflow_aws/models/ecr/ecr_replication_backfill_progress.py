from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ECRReplicationBackfillProgress(BaseModel):
    totalReplicationCount: StrictInt | None = None
    completedReplicationCount: StrictInt | None = None
    failedReplicationCount: StrictInt | None = None
    failureCodes: list[StrictStr] | None = None
