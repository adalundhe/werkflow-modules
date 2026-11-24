from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class DataZoneCreateDesignationRequest(BaseModel):
    domainIdentifier: StrictStr
    name: StrictStr
    policy: StrictStr
    description: StrictStr | None = None
    deletionProtection: StrictBool | None = None
