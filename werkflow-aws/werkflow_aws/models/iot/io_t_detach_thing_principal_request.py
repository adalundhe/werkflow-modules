from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTDetachThingPrincipalRequest(BaseModel):
    thingName: StrictStr
    principal: StrictStr
