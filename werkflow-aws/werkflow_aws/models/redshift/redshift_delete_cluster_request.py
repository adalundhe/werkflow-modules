from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class RedshiftDeleteClusterRequest(BaseModel):
    ClusterIdentifier: StrictStr
    SkipFinalClusterSnapshot: StrictBool | None = None
    FinalClusterSnapshotIdentifier: StrictStr | None = None
    FinalClusterSnapshotRetentionPeriod: StrictInt | None = None
