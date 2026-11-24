from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class DeviceFarmUpdateInstanceProfileRequest(BaseModel):
    arn: StrictStr
    name: StrictStr | None = None
    description: StrictStr | None = None
    packageCleanup: StrictBool | None = None
    excludeAppPackagesFromCleanup: list[StrictStr] | None = None
    rebootAfterUse: StrictBool | None = None
