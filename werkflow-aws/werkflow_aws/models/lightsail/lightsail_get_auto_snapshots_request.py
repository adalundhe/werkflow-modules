from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LightsailGetAutoSnapshotsRequest(BaseModel):
    resourceName: StrictStr
