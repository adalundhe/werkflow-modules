from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudSearchCreateDomainRequest(BaseModel):
    DomainName: StrictStr
