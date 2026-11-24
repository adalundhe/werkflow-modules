from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayDeleteBasePathMappingRequest(BaseModel):
    domainName: StrictStr
    basePath: StrictStr
    domainNameId: StrictStr | None = None
