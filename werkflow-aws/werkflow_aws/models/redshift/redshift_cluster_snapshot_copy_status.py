from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class RedshiftClusterSnapshotCopyStatus(BaseModel):
    DestinationRegion: StrictStr | None = None
    RetentionPeriod: StrictInt | None = None
    ManualSnapshotRetentionPeriod: StrictInt | None = None
    SnapshotCopyGrantName: StrictStr | None = None
