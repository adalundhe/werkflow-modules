from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .device_farm_project import DeviceFarmProject


class DeviceFarmListProjectsResponse(BaseModel):
    projects: list[DeviceFarmProject] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
