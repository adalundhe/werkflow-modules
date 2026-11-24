from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppSyncGetApiAssociationRequest(BaseModel):
    domainName: StrictStr
