from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LightsailDeleteAutoSnapshotRequest(BaseModel):
    resourceName: StrictStr
    date: StrictStr
