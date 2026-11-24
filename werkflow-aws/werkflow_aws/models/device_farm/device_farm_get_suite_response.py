from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .device_farm_suite import DeviceFarmSuite


class DeviceFarmGetSuiteResponse(BaseModel):
    suite: DeviceFarmSuite | None = None
    ResponseMetadata: dict[str, Any] | None = None
