from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayV2PreviewPortalRequest(BaseModel):
    PortalId: StrictStr
