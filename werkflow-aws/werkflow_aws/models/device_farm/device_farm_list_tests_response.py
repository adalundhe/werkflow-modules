from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .device_farm_test import DeviceFarmTest


class DeviceFarmListTestsResponse(BaseModel):
    tests: list[DeviceFarmTest] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
