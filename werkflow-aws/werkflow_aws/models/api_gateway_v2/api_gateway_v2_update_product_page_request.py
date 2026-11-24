from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .api_gateway_v2_display_content import APIGatewayV2DisplayContent


class APIGatewayV2UpdateProductPageRequest(BaseModel):
    PortalProductId: StrictStr
    ProductPageId: StrictStr
    DisplayContent: APIGatewayV2DisplayContent | None = None
