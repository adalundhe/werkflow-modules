from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class EC2InstanceCapacity(BaseModel):
    AvailableCapacity: StrictInt | None = None
    InstanceType: StrictStr | None = None
    TotalCapacity: StrictInt | None = None
