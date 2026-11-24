from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .api_gateway_v2_authorization import APIGatewayV2Authorization
from .api_gateway_v2_endpoint_configuration_request import APIGatewayV2EndpointConfigurationRequest
from .api_gateway_v2_portal_content import APIGatewayV2PortalContent


class APIGatewayV2UpdatePortalRequest(BaseModel):
    PortalId: StrictStr
    Authorization: APIGatewayV2Authorization | None = None
    EndpointConfiguration: APIGatewayV2EndpointConfigurationRequest | None = None
    IncludedPortalProductArns: list[StrictStr] | None = None
    LogoUri: StrictStr | None = None
    PortalContent: APIGatewayV2PortalContent | None = None
    RumAppMonitorName: StrictStr | None = None
