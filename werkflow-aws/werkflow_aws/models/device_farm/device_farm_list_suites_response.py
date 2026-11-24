from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .device_farm_suite import DeviceFarmSuite


class DeviceFarmListSuitesResponse(BaseModel):
    suites: list[DeviceFarmSuite] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
