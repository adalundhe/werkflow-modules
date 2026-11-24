from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayV2CreateApiMappingRequest(BaseModel):
    ApiId: StrictStr
    DomainName: StrictStr
    Stage: StrictStr
    ApiMappingKey: StrictStr | None = None
