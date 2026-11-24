from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .api_gateway_v2_display_order import APIGatewayV2DisplayOrder


class APIGatewayV2UpdatePortalProductRequest(BaseModel):
    PortalProductId: StrictStr
    Description: StrictStr | None = None
    DisplayName: StrictStr | None = None
    DisplayOrder: APIGatewayV2DisplayOrder | None = None
