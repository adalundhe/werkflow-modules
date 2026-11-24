from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayGetResourceRequest(BaseModel):
    restApiId: StrictStr
    resourceId: StrictStr
    embed: list[StrictStr] | None = None
