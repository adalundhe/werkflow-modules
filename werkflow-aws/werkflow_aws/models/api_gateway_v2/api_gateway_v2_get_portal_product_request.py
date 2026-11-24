from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayV2GetPortalProductRequest(BaseModel):
    PortalProductId: StrictStr
    ResourceOwnerAccountId: StrictStr | None = None
