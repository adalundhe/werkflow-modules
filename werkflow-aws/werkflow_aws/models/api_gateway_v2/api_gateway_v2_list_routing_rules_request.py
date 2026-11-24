from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class APIGatewayV2ListRoutingRulesRequest(BaseModel):
    DomainName: StrictStr
    DomainNameId: StrictStr | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
