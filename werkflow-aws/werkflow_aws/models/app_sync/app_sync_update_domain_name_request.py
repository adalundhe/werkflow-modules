from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppSyncUpdateDomainNameRequest(BaseModel):
    domainName: StrictStr
    description: StrictStr | None = None
