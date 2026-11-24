from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class RedshiftModifySnapshotCopyRetentionPeriodRequest(BaseModel):
    ClusterIdentifier: StrictStr
    RetentionPeriod: StrictInt
    Manual: StrictBool | None = None
