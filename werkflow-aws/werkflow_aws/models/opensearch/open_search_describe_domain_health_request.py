from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchDescribeDomainHealthRequest(BaseModel):
    DomainName: StrictStr
