from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayGetRestApiRequest(BaseModel):
    restApiId: StrictStr
