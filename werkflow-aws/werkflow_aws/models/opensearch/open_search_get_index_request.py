from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchGetIndexRequest(BaseModel):
    DomainName: StrictStr
    IndexName: StrictStr
