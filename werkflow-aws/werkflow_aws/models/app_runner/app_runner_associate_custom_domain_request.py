from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class AppRunnerAssociateCustomDomainRequest(BaseModel):
    ServiceArn: StrictStr
    DomainName: StrictStr
    EnableWWWSubdomain: StrictBool | None = None
