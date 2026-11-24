from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchDeleteIndexRequest(BaseModel):
    DomainName: StrictStr
    IndexName: StrictStr
