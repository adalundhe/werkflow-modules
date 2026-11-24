from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AmplifyGetDomainAssociationRequest(BaseModel):
    appId: StrictStr
    domainName: StrictStr
