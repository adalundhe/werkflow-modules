from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LightsailDeleteRelationalDatabaseSnapshotRequest(BaseModel):
    relationalDatabaseSnapshotName: StrictStr
