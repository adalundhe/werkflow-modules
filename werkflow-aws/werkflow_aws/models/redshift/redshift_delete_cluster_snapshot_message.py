from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RedshiftDeleteClusterSnapshotMessage(BaseModel):
    SnapshotIdentifier: StrictStr
    SnapshotClusterIdentifier: StrictStr | None = None
