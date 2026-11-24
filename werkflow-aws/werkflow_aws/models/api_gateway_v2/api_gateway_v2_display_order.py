from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .api_gateway_v2_section import APIGatewayV2Section


class APIGatewayV2DisplayOrder(BaseModel):
    Contents: list[APIGatewayV2Section] | None = None
    OverviewPageArn: StrictStr | None = None
    ProductPageArns: list[StrictStr] | None = None
