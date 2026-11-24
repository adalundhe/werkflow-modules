from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class DataZoneGetConnectionRequest(BaseModel):
    domainIdentifier: StrictStr
    identifier: StrictStr
    withSecret: StrictBool | None = None
