from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FSxOpenZFSOriginSnapshotConfiguration(BaseModel):
    SnapshotARN: StrictStr | None = None
    CopyStrategy: StrictStr | None = None
