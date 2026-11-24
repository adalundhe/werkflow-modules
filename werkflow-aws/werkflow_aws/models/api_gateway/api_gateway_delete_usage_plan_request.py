from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayDeleteUsagePlanRequest(BaseModel):
    usagePlanId: StrictStr
