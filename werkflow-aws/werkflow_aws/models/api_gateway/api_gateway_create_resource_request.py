from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayCreateResourceRequest(BaseModel):
    restApiId: StrictStr
    parentId: StrictStr
    pathPart: StrictStr
