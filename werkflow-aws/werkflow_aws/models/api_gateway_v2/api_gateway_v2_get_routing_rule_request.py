from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayV2GetRoutingRuleRequest(BaseModel):
    DomainName: StrictStr
    RoutingRuleId: StrictStr
    DomainNameId: StrictStr | None = None
