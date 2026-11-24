from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayV2RoutingRuleMatchHeaderValue(BaseModel):
    Header: StrictStr | None = None
    ValueGlob: StrictStr | None = None
