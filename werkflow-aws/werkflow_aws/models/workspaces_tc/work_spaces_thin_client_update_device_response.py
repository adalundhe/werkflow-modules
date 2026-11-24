from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .work_spaces_thin_client_device_summary import WorkSpacesThinClientDeviceSummary


class WorkSpacesThinClientUpdateDeviceResponse(BaseModel):
    device: WorkSpacesThinClientDeviceSummary | None = None
    ResponseMetadata: dict[str, Any] | None = None
