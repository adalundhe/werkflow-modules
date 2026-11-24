from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectDeviceInfo(BaseModel):
    PlatformName: StrictStr | None = None
    PlatformVersion: StrictStr | None = None
    OperatingSystem: StrictStr | None = None
