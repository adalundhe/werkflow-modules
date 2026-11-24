from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppRunnerDisassociateCustomDomainRequest(BaseModel):
    ServiceArn: StrictStr
    DomainName: StrictStr
