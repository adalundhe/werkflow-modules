from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SimpleDBDomainMetadataRequest(BaseModel):
    DomainName: StrictStr
