from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayGetUsagePlanKeyRequest(BaseModel):
    usagePlanId: StrictStr
    keyId: StrictStr
