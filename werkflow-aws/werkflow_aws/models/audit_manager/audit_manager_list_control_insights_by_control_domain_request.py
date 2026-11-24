from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class AuditManagerListControlInsightsByControlDomainRequest(BaseModel):
    controlDomainId: StrictStr
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
