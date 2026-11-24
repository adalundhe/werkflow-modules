from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .device_farm_project import DeviceFarmProject


class DeviceFarmUpdateProjectResponse(BaseModel):
    project: DeviceFarmProject | None = None
    ResponseMetadata: dict[str, Any] | None = None
