from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppSyncDeleteDomainNameRequest(BaseModel):
    domainName: StrictStr
