from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .security_hub_aws_api_gateway_access_log_settings import SecurityHubAwsApiGatewayAccessLogSettings
from .security_hub_aws_api_gateway_v2_route_settings import SecurityHubAwsApiGatewayV2RouteSettings


class SecurityHubAwsApiGatewayV2StageDetails(BaseModel):
    ClientCertificateId: StrictStr | None = None
    CreatedDate: StrictStr | None = None
    Description: StrictStr | None = None
    DefaultRouteSettings: SecurityHubAwsApiGatewayV2RouteSettings | None = None
    DeploymentId: StrictStr | None = None
    LastUpdatedDate: StrictStr | None = None
    RouteSettings: SecurityHubAwsApiGatewayV2RouteSettings | None = None
    StageName: StrictStr | None = None
    StageVariables: dict[StrictStr, StrictStr] | None = None
    AccessLogSettings: SecurityHubAwsApiGatewayAccessLogSettings | None = None
    AutoDeploy: StrictBool | None = None
    LastDeploymentStatusMessage: StrictStr | None = None
    ApiGatewayManaged: StrictBool | None = None
