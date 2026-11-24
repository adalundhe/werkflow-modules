from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayV2DeleteProductPageRequest(BaseModel):
    PortalProductId: StrictStr
    ProductPageId: StrictStr
