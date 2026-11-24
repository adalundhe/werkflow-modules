from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class DeviceFarmInstanceProfile(BaseModel):
    arn: StrictStr | None = None
    packageCleanup: StrictBool | None = None
    excludeAppPackagesFromCleanup: list[StrictStr] | None = None
    rebootAfterUse: StrictBool | None = None
    name: StrictStr | None = None
    description: StrictStr | None = None
