from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchDescribeDomainRequest(BaseModel):
    DomainName: StrictStr
