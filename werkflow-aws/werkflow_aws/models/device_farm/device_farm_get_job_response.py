from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .device_farm_job import DeviceFarmJob


class DeviceFarmGetJobResponse(BaseModel):
    job: DeviceFarmJob | None = None
    ResponseMetadata: dict[str, Any] | None = None
