from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .iam_tag_model import IAMTagModel


class IAMCreateVirtualMFADeviceRequest(BaseModel):
    VirtualMFADeviceName: StrictStr
    Path: StrictStr | None = None
    Tags: list[IAMTagModel] | None = None
