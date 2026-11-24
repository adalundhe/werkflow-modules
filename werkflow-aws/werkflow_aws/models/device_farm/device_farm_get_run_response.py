from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .device_farm_run import DeviceFarmRun


class DeviceFarmGetRunResponse(BaseModel):
    run: DeviceFarmRun | None = None
    ResponseMetadata: dict[str, Any] | None = None
