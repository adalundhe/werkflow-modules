from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .device_farm_test import DeviceFarmTest


class DeviceFarmGetTestResponse(BaseModel):
    test: DeviceFarmTest | None = None
    ResponseMetadata: dict[str, Any] | None = None
