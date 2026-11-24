from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneDeleteFormTypeRequest(BaseModel):
    domainIdentifier: StrictStr
    formTypeIdentifier: StrictStr
