from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lightsail_tag import LightsailTag


class LightsailCreateInstanceSnapshotRequest(BaseModel):
    instanceSnapshotName: StrictStr
    instanceName: StrictStr
    tags: list[LightsailTag] | None = None
