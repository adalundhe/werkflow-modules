from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RedshiftDisableSnapshotCopyRequest(BaseModel):
    ClusterIdentifier: StrictStr
