from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class RedshiftEnableSnapshotCopyRequest(BaseModel):
    ClusterIdentifier: StrictStr
    DestinationRegion: StrictStr
    RetentionPeriod: StrictInt | None = None
    SnapshotCopyGrantName: StrictStr | None = None
    ManualSnapshotRetentionPeriod: StrictInt | None = None
