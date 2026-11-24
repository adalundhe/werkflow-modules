from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class IoTDeleteThingRequest(BaseModel):
    thingName: StrictStr
    expectedVersion: StrictInt | None = None
