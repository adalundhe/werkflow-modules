from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .api_gateway_v2_product_page_summary_no_body import APIGatewayV2ProductPageSummaryNoBody


class APIGatewayV2ListProductPagesResponse(BaseModel):
    Items: list[APIGatewayV2ProductPageSummaryNoBody] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
