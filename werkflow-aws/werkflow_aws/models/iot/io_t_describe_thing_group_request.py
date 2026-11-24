from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTDescribeThingGroupRequest(BaseModel):
    thingGroupName: StrictStr
