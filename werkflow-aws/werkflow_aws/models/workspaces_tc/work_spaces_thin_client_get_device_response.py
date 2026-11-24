from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .work_spaces_thin_client_device import WorkSpacesThinClientDevice


class WorkSpacesThinClientGetDeviceResponse(BaseModel):
    device: WorkSpacesThinClientDevice | None = None
    ResponseMetadata: dict[str, Any] | None = None
