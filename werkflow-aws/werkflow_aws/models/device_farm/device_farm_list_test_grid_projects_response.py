from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .device_farm_test_grid_project import DeviceFarmTestGridProject


class DeviceFarmListTestGridProjectsResponse(BaseModel):
    testGridProjects: list[DeviceFarmTestGridProject] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
