from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .security_hub_aws_api_gateway_access_log_settings import SecurityHubAwsApiGatewayAccessLogSettings
from .security_hub_aws_api_gateway_canary_settings import SecurityHubAwsApiGatewayCanarySettings
from .security_hub_aws_api_gateway_method_settings import SecurityHubAwsApiGatewayMethodSettings


class SecurityHubAwsApiGatewayStageDetails(BaseModel):
    DeploymentId: StrictStr | None = None
    ClientCertificateId: StrictStr | None = None
    StageName: StrictStr | None = None
    Description: StrictStr | None = None
    CacheClusterEnabled: StrictBool | None = None
    CacheClusterSize: StrictStr | None = None
    CacheClusterStatus: StrictStr | None = None
    MethodSettings: list[SecurityHubAwsApiGatewayMethodSettings] | None = None
    Variables: dict[StrictStr, StrictStr] | None = None
    DocumentationVersion: StrictStr | None = None
    AccessLogSettings: SecurityHubAwsApiGatewayAccessLogSettings | None = None
    CanarySettings: SecurityHubAwsApiGatewayCanarySettings | None = None
    TracingEnabled: StrictBool | None = None
    CreatedDate: StrictStr | None = None
    LastUpdatedDate: StrictStr | None = None
    WebAclArn: StrictStr | None = None
