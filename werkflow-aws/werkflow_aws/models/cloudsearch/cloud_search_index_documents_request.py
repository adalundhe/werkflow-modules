from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudSearchIndexDocumentsRequest(BaseModel):
    DomainName: StrictStr
