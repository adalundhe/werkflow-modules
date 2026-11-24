from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SimpleDBDeleteDomainRequest(BaseModel):
    DomainName: StrictStr
