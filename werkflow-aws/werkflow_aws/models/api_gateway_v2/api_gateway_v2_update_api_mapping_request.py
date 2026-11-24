from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayV2UpdateApiMappingRequest(BaseModel):
    ApiId: StrictStr
    ApiMappingId: StrictStr
    DomainName: StrictStr
    ApiMappingKey: StrictStr | None = None
    Stage: StrictStr | None = None
