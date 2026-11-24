from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_aws_cors_configuration import SecurityHubAwsCorsConfiguration


class SecurityHubAwsApiGatewayV2ApiDetails(BaseModel):
    ApiEndpoint: StrictStr | None = None
    ApiId: StrictStr | None = None
    ApiKeySelectionExpression: StrictStr | None = None
    CreatedDate: StrictStr | None = None
    Description: StrictStr | None = None
    Version: StrictStr | None = None
    Name: StrictStr | None = None
    ProtocolType: StrictStr | None = None
    RouteSelectionExpression: StrictStr | None = None
    CorsConfiguration: SecurityHubAwsCorsConfiguration | None = None
