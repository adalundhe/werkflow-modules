from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayGetUsagePlanRequest(BaseModel):
    usagePlanId: StrictStr
