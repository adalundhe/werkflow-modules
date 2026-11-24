from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayV2RoutingRuleMatchBasePaths(BaseModel):
    AnyOf: list[StrictStr] | None = None
