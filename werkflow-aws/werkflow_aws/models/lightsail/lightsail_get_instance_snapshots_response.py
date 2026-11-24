from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .lightsail_instance_snapshot import LightsailInstanceSnapshot


class LightsailGetInstanceSnapshotsResponse(BaseModel):
    instanceSnapshots: list[LightsailInstanceSnapshot] | None = None
    nextPageToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
