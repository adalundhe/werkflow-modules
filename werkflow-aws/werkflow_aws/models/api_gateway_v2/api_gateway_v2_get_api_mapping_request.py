from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayV2GetApiMappingRequest(BaseModel):
    ApiMappingId: StrictStr
    DomainName: StrictStr
