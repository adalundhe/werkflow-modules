from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudSearchDeleteDomainRequest(BaseModel):
    DomainName: StrictStr
