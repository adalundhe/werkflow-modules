from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .api_gateway_v2_endpoint_display_content import APIGatewayV2EndpointDisplayContent


class APIGatewayV2UpdateProductRestEndpointPageRequest(BaseModel):
    PortalProductId: StrictStr
    ProductRestEndpointPageId: StrictStr
    DisplayContent: APIGatewayV2EndpointDisplayContent | None = None
    TryItState: Literal['ENABLED', 'DISABLED'] | None = None
