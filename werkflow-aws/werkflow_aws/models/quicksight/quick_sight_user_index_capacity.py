from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightUserIndexCapacity(BaseModel):
    userArn: StrictStr | None = None
    userName: StrictStr | None = None
    email: StrictStr | None = None
    role: StrictStr | None = None
    totalCapacityBytes: StrictInt | None = None
    totalKBCapacityBytes: StrictInt | None = None
    totalSpaceCapacityBytes: StrictInt | None = None
    kbCount: StrictInt | None = None
    spaceCount: StrictInt | None = None
