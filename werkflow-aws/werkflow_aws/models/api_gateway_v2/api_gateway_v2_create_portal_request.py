from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .api_gateway_v2_authorization import APIGatewayV2Authorization
from .api_gateway_v2_endpoint_configuration_request import APIGatewayV2EndpointConfigurationRequest
from .api_gateway_v2_portal_content import APIGatewayV2PortalContent


class APIGatewayV2CreatePortalRequest(BaseModel):
    Authorization: APIGatewayV2Authorization
    EndpointConfiguration: APIGatewayV2EndpointConfigurationRequest
    PortalContent: APIGatewayV2PortalContent
    IncludedPortalProductArns: list[StrictStr] | None = None
    LogoUri: StrictStr | None = None
    RumAppMonitorName: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
