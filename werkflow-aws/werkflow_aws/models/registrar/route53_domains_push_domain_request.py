from __future__ import annotations
from pydantic import BaseModel, StrictStr


class Route53DomainsPushDomainRequest(BaseModel):
    DomainName: StrictStr
    Target: StrictStr
