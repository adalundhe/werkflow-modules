from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .device_farm_test_grid_session_artifact import DeviceFarmTestGridSessionArtifact


class DeviceFarmListTestGridSessionArtifactsResponse(BaseModel):
    artifacts: list[DeviceFarmTestGridSessionArtifact] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
