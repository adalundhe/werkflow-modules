from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayDeleteRestApiRequest(BaseModel):
    restApiId: StrictStr
