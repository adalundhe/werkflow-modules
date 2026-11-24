from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneOwnerUserProperties(BaseModel):
    userIdentifier: StrictStr
