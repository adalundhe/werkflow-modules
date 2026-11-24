from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .iam_tag_model import IAMTagModel


class IAMTagMFADeviceRequest(BaseModel):
    SerialNumber: StrictStr
    Tags: list[IAMTagModel]
