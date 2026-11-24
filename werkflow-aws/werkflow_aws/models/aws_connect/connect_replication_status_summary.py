from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectReplicationStatusSummary(BaseModel):
    Region: StrictStr | None = None
    ReplicationStatus: StrictStr | None = None
    ReplicationStatusReason: StrictStr | None = None
