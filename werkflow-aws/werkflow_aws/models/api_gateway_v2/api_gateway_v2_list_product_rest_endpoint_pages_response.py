from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .api_gateway_v2_product_rest_endpoint_page_summary_no_body import APIGatewayV2ProductRestEndpointPageSummaryNoBody


class APIGatewayV2ListProductRestEndpointPagesResponse(BaseModel):
    Items: list[APIGatewayV2ProductRestEndpointPageSummaryNoBody] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
