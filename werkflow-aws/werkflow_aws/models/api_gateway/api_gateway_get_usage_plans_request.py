from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class APIGatewayGetUsagePlansRequest(BaseModel):
    position: StrictStr | None = None
    keyId: StrictStr | None = None
    limit: StrictInt | None = None
