from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTDescribeThingTypeRequest(BaseModel):
    thingTypeName: StrictStr
