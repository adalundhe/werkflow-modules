from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .device_farm_run import DeviceFarmRun


class DeviceFarmListRunsResponse(BaseModel):
    runs: list[DeviceFarmRun] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
