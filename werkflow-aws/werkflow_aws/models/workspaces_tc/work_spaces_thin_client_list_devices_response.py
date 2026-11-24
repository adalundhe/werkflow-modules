from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .work_spaces_thin_client_device_summary import WorkSpacesThinClientDeviceSummary


class WorkSpacesThinClientListDevicesResponse(BaseModel):
    devices: list[WorkSpacesThinClientDeviceSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
