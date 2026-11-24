from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LightsailGetDomainRequest(BaseModel):
    domainName: StrictStr
