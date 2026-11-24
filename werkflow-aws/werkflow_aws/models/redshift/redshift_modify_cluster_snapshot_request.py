from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class RedshiftModifyClusterSnapshotRequest(BaseModel):
    SnapshotIdentifier: StrictStr
    ManualSnapshotRetentionPeriod: StrictInt | None = None
    Force: StrictBool | None = None
