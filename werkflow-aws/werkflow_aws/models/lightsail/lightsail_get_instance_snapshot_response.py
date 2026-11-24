from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .lightsail_instance_snapshot import LightsailInstanceSnapshot


class LightsailGetInstanceSnapshotResponse(BaseModel):
    instanceSnapshot: LightsailInstanceSnapshot | None = None
    ResponseMetadata: dict[str, Any] | None = None
