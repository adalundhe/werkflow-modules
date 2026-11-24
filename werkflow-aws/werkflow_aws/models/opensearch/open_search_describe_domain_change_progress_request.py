from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchDescribeDomainChangeProgressRequest(BaseModel):
    DomainName: StrictStr
    ChangeId: StrictStr | None = None
