from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class APIGatewayGetUsageRequest(BaseModel):
    usagePlanId: StrictStr
    startDate: StrictStr
    endDate: StrictStr
    keyId: StrictStr | None = None
    position: StrictStr | None = None
    limit: StrictInt | None = None
