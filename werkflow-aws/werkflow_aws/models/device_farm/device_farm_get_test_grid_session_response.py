from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .device_farm_test_grid_session import DeviceFarmTestGridSession


class DeviceFarmGetTestGridSessionResponse(BaseModel):
    testGridSession: DeviceFarmTestGridSession | None = None
    ResponseMetadata: dict[str, Any] | None = None
