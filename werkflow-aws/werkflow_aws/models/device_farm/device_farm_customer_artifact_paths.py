from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DeviceFarmCustomerArtifactPaths(BaseModel):
    iosPaths: list[StrictStr] | None = None
    androidPaths: list[StrictStr] | None = None
    deviceHostPaths: list[StrictStr] | None = None
