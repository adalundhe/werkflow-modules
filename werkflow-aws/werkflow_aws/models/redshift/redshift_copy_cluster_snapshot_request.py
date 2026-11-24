from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class RedshiftCopyClusterSnapshotRequest(BaseModel):
    SourceSnapshotIdentifier: StrictStr
    TargetSnapshotIdentifier: StrictStr
    SourceSnapshotClusterIdentifier: StrictStr | None = None
    ManualSnapshotRetentionPeriod: StrictInt | None = None
