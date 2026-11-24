from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LightsailDeleteDomainRequest(BaseModel):
    domainName: StrictStr
