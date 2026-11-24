from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayV2PublishPortalRequest(BaseModel):
    PortalId: StrictStr
    Description: StrictStr | None = None
