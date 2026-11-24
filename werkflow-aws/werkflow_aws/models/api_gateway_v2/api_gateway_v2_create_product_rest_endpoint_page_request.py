from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .api_gateway_v2_endpoint_display_content import APIGatewayV2EndpointDisplayContent
from .api_gateway_v2_rest_endpoint_identifier import APIGatewayV2RestEndpointIdentifier


class APIGatewayV2CreateProductRestEndpointPageRequest(BaseModel):
    PortalProductId: StrictStr
    RestEndpointIdentifier: APIGatewayV2RestEndpointIdentifier
    DisplayContent: APIGatewayV2EndpointDisplayContent | None = None
    TryItState: Literal['ENABLED', 'DISABLED'] | None = None
