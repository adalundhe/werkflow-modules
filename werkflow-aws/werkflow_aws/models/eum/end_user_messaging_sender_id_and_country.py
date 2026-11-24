from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EndUserMessagingSenderIdAndCountry(BaseModel):
    SenderId: StrictStr
    IsoCountryCode: StrictStr
