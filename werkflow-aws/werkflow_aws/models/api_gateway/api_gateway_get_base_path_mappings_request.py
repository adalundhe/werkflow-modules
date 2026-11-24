from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class APIGatewayGetBasePathMappingsRequest(BaseModel):
    domainName: StrictStr
    domainNameId: StrictStr | None = None
    position: StrictStr | None = None
    limit: StrictInt | None = None
