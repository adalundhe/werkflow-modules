from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SecurityHubAwsRedshiftClusterClusterSnapshotCopyStatus(BaseModel):
    DestinationRegion: StrictStr | None = None
    ManualSnapshotRetentionPeriod: StrictInt | None = None
    RetentionPeriod: StrictInt | None = None
    SnapshotCopyGrantName: StrictStr | None = None
