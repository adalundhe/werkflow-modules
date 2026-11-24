from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayCreateBasePathMappingRequest(BaseModel):
    domainName: StrictStr
    restApiId: StrictStr
    domainNameId: StrictStr | None = None
    basePath: StrictStr | None = None
    stage: StrictStr | None = None
