from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .iammfa_device import IAMMFADevice


class IAMListMFADevicesResponse(BaseModel):
    MFADevices: list[IAMMFADevice] | None = None
    IsTruncated: StrictBool | None = None
    Marker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
