from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayDeleteUsagePlanKeyRequest(BaseModel):
    usagePlanId: StrictStr
    keyId: StrictStr
