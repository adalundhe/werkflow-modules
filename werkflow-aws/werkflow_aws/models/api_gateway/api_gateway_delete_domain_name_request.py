from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayDeleteDomainNameRequest(BaseModel):
    domainName: StrictStr
    domainNameId: StrictStr | None = None
