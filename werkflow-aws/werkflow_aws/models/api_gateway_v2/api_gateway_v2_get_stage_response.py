from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .api_gateway_v2_access_log_settings import APIGatewayV2AccessLogSettings
from .api_gateway_v2_route_settings import APIGatewayV2RouteSettings


class APIGatewayV2GetStageResponse(BaseModel):
    AccessLogSettings: APIGatewayV2AccessLogSettings | None = None
    ApiGatewayManaged: StrictBool | None = None
    AutoDeploy: StrictBool | None = None
    ClientCertificateId: StrictStr | None = None
    CreatedDate: datetime.datetime | StrictStr | None = None
    DefaultRouteSettings: APIGatewayV2RouteSettings | None = None
    DeploymentId: StrictStr | None = None
    Description: StrictStr | None = None
    LastDeploymentStatusMessage: StrictStr | None = None
    LastUpdatedDate: datetime.datetime | StrictStr | None = None
    RouteSettings: dict[StrictStr, APIGatewayV2RouteSettings] | None = None
    StageName: StrictStr | None = None
    StageVariables: dict[StrictStr, StrictStr] | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
