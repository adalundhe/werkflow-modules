from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class DataZoneUpdateGroupProfileRequest(BaseModel):
    domainIdentifier: StrictStr
    groupIdentifier: StrictStr
    status: Literal['ASSIGNED', 'NOT_ASSIGNED']
