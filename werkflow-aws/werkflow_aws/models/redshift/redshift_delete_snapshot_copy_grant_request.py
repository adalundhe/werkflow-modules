from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RedshiftDeleteSnapshotCopyGrantRequest(BaseModel):
    SnapshotCopyGrantName: StrictStr
