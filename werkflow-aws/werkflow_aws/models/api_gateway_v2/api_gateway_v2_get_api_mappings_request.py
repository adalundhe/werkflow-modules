from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayV2GetApiMappingsRequest(BaseModel):
    DomainName: StrictStr
    MaxResults: StrictStr | None = None
    NextToken: StrictStr | None = None
