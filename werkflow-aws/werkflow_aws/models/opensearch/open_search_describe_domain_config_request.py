from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchDescribeDomainConfigRequest(BaseModel):
    DomainName: StrictStr
