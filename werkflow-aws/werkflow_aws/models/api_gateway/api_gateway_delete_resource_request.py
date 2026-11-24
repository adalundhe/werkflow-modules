from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayDeleteResourceRequest(BaseModel):
    restApiId: StrictStr
    resourceId: StrictStr
