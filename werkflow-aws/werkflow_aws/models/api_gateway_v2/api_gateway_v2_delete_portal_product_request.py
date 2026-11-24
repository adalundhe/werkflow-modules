from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayV2DeletePortalProductRequest(BaseModel):
    PortalProductId: StrictStr
