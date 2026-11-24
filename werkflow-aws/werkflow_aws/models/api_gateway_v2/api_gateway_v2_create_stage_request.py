from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .api_gateway_v2_access_log_settings import APIGatewayV2AccessLogSettings
from .api_gateway_v2_route_settings import APIGatewayV2RouteSettings


class APIGatewayV2CreateStageRequest(BaseModel):
    ApiId: StrictStr
    StageName: StrictStr
    AccessLogSettings: APIGatewayV2AccessLogSettings | None = None
    AutoDeploy: StrictBool | None = None
    ClientCertificateId: StrictStr | None = None
    DefaultRouteSettings: APIGatewayV2RouteSettings | None = None
    DeploymentId: StrictStr | None = None
    Description: StrictStr | None = None
    RouteSettings: dict[StrictStr, APIGatewayV2RouteSettings] | None = None
    StageVariables: dict[StrictStr, StrictStr] | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
