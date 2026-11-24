from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppSyncGetDomainNameRequest(BaseModel):
    domainName: StrictStr
