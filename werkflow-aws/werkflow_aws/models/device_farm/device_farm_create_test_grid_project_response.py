from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .device_farm_test_grid_project import DeviceFarmTestGridProject


class DeviceFarmCreateTestGridProjectResponse(BaseModel):
    testGridProject: DeviceFarmTestGridProject | None = None
    ResponseMetadata: dict[str, Any] | None = None
