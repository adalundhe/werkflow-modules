from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayCreateUsagePlanKeyRequest(BaseModel):
    usagePlanId: StrictStr
    keyId: StrictStr
    keyType: StrictStr
