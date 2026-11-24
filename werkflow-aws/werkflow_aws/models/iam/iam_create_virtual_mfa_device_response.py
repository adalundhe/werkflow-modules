from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .iam_virtual_mfa_device import IAMVirtualMFADevice


class IAMCreateVirtualMFADeviceResponse(BaseModel):
    VirtualMFADevice: IAMVirtualMFADevice | None = None
    ResponseMetadata: dict[str, Any] | None = None
