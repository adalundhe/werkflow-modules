from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class DataZoneUpdateDesignationRequest(BaseModel):
    domainIdentifier: StrictStr
    identifier: StrictStr
    name: StrictStr | None = None
    description: StrictStr | None = None
    policy: StrictStr | None = None
    deletionProtection: StrictBool | None = None
