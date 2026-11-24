from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FSxDeleteSnapshotRequest(BaseModel):
    SnapshotId: StrictStr
    ClientRequestToken: StrictStr | None = None
