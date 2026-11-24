from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchGetCompatibleVersionsRequest(BaseModel):
    DomainName: StrictStr | None = None
