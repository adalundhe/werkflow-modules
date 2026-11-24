from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RedshiftDeleteClusterSnapshotRequest(BaseModel):
    SnapshotIdentifier: StrictStr
    SnapshotClusterIdentifier: StrictStr | None = None
