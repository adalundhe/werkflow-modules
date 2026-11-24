from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ElasticacheDeleteSnapshotRequest(BaseModel):
    SnapshotName: StrictStr
