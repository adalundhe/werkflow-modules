from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lightsail_tag import LightsailTag


class LightsailCreateDiskSnapshotRequest(BaseModel):
    diskSnapshotName: StrictStr
    diskName: StrictStr | None = None
    instanceName: StrictStr | None = None
    tags: list[LightsailTag] | None = None
