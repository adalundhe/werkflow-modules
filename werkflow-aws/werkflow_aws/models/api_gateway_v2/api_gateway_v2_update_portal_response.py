from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .api_gateway_v2_authorization import APIGatewayV2Authorization
from .api_gateway_v2_endpoint_configuration_response import APIGatewayV2EndpointConfigurationResponse
from .api_gateway_v2_portal_content import APIGatewayV2PortalContent
from .api_gateway_v2_preview import APIGatewayV2Preview
from .api_gateway_v2_status_exception import APIGatewayV2StatusException


class APIGatewayV2UpdatePortalResponse(BaseModel):
    Authorization: APIGatewayV2Authorization | None = None
    EndpointConfiguration: APIGatewayV2EndpointConfigurationResponse | None = None
    IncludedPortalProductArns: list[StrictStr] | None = None
    LastModified: datetime.datetime | StrictStr | None = None
    LastPublished: datetime.datetime | StrictStr | None = None
    LastPublishedDescription: StrictStr | None = None
    PortalArn: StrictStr | None = None
    PortalContent: APIGatewayV2PortalContent | None = None
    PortalId: StrictStr | None = None
    Preview: APIGatewayV2Preview | None = None
    PublishStatus: StrictStr | None = None
    RumAppMonitorName: StrictStr | None = None
    StatusException: APIGatewayV2StatusException | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
