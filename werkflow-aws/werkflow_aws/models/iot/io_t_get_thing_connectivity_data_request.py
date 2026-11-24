from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class IoTGetThingConnectivityDataRequest(BaseModel):
    thingName: StrictStr
    includeSocketInformation: StrictBool | None = None
