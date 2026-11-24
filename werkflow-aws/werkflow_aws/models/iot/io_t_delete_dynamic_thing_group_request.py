from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class IoTDeleteDynamicThingGroupRequest(BaseModel):
    thingGroupName: StrictStr
    expectedVersion: StrictInt | None = None
