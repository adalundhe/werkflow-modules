from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTDeleteThingTypeRequest(BaseModel):
    thingTypeName: StrictStr
