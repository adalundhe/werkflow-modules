from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class IoTDeleteThingGroupRequest(BaseModel):
    thingGroupName: StrictStr
    expectedVersion: StrictInt | None = None
