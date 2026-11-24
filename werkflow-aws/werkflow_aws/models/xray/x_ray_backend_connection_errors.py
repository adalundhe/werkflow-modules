from __future__ import annotations
from pydantic import BaseModel, StrictInt


class XRayBackendConnectionErrors(BaseModel):
    TimeoutCount: StrictInt | None = None
    ConnectionRefusedCount: StrictInt | None = None
    HTTPCode4XXCount: StrictInt | None = None
    HTTPCode5XXCount: StrictInt | None = None
    UnknownHostCount: StrictInt | None = None
    OtherCount: StrictInt | None = None
