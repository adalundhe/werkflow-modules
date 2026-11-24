from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class LocationWiFiAccessPoint(BaseModel):
    MacAddress: StrictStr
    Rss: StrictInt
