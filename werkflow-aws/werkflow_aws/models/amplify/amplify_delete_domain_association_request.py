from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AmplifyDeleteDomainAssociationRequest(BaseModel):
    appId: StrictStr
    domainName: StrictStr
