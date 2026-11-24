from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class RedshiftBatchModifyClusterSnapshotsRequest(BaseModel):
    SnapshotIdentifierList: list[StrictStr]
    ManualSnapshotRetentionPeriod: StrictInt | None = None
    Force: StrictBool | None = None
