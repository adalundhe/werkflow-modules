from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .lightsail_disk_snapshot import LightsailDiskSnapshot


class LightsailGetDiskSnapshotResponse(BaseModel):
    diskSnapshot: LightsailDiskSnapshot | None = None
    ResponseMetadata: dict[str, Any] | None = None
