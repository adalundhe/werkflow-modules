from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class APIGatewayGetUsagePlanKeysRequest(BaseModel):
    usagePlanId: StrictStr
    position: StrictStr | None = None
    limit: StrictInt | None = None
    nameQuery: StrictStr | None = None
