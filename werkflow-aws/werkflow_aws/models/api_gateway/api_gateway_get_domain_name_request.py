from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayGetDomainNameRequest(BaseModel):
    domainName: StrictStr
    domainNameId: StrictStr | None = None
