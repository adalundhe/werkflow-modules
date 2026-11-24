from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppSyncAssociateApiRequest(BaseModel):
    domainName: StrictStr
    apiId: StrictStr
