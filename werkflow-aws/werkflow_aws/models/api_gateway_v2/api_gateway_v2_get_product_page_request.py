from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayV2GetProductPageRequest(BaseModel):
    PortalProductId: StrictStr
    ProductPageId: StrictStr
    ResourceOwnerAccountId: StrictStr | None = None
