from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .lightsail_disk_snapshot import LightsailDiskSnapshot


class LightsailGetDiskSnapshotsResponse(BaseModel):
    diskSnapshots: list[LightsailDiskSnapshot] | None = None
    nextPageToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
