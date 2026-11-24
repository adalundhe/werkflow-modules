from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .device_farm_artifact import DeviceFarmArtifact


class DeviceFarmListArtifactsResponse(BaseModel):
    artifacts: list[DeviceFarmArtifact] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
