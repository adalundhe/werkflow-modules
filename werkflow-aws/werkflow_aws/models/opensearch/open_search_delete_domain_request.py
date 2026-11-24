from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchDeleteDomainRequest(BaseModel):
    DomainName: StrictStr
