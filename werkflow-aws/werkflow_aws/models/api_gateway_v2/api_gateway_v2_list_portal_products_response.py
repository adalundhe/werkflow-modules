from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .api_gateway_v2_portal_product_summary import APIGatewayV2PortalProductSummary


class APIGatewayV2ListPortalProductsResponse(BaseModel):
    Items: list[APIGatewayV2PortalProductSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
