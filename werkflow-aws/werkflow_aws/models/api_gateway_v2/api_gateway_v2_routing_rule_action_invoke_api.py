from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class APIGatewayV2RoutingRuleActionInvokeApi(BaseModel):
    ApiId: StrictStr | None = None
    Stage: StrictStr | None = None
    StripBasePath: StrictBool | None = None
