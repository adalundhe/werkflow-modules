from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class LightsailCheckSubdomainAvailabilityRequest(BaseModel):
    subdomainName: StrictStr
    reserve: StrictBool | None = None
