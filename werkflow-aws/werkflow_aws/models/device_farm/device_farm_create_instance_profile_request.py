from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class DeviceFarmCreateInstanceProfileRequest(BaseModel):
    name: StrictStr
    description: StrictStr | None = None
    packageCleanup: StrictBool | None = None
    excludeAppPackagesFromCleanup: list[StrictStr] | None = None
    rebootAfterUse: StrictBool | None = None
