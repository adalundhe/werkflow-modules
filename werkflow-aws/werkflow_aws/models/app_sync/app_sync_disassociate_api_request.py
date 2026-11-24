from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppSyncDisassociateApiRequest(BaseModel):
    domainName: StrictStr
