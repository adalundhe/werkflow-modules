from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class DeviceFarmDeviceProxy(BaseModel):
    host: StrictStr | None = None
    port: StrictInt | None = None
