from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayV2DeletePortalRequest(BaseModel):
    PortalId: StrictStr
