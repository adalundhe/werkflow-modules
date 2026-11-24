from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .iam_virtual_mfa_device import IAMVirtualMFADevice


class IAMListVirtualMFADevicesResponse(BaseModel):
    VirtualMFADevices: list[IAMVirtualMFADevice] | None = None
    IsTruncated: StrictBool | None = None
    Marker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
