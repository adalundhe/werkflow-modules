from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayV2GetPortalRequest(BaseModel):
    PortalId: StrictStr
