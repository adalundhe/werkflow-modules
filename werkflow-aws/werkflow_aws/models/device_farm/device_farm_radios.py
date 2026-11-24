from __future__ import annotations
from pydantic import BaseModel, StrictBool


class DeviceFarmRadios(BaseModel):
    wifi: StrictBool | None = None
    bluetooth: StrictBool | None = None
    nfc: StrictBool | None = None
    gps: StrictBool | None = None
