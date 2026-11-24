from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneOwnerGroupProperties(BaseModel):
    groupIdentifier: StrictStr
