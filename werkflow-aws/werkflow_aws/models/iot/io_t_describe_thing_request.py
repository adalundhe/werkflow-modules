from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTDescribeThingRequest(BaseModel):
    thingName: StrictStr
