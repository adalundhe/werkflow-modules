from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .security_hub_aws_api_gateway_endpoint_configuration import SecurityHubAwsApiGatewayEndpointConfiguration


class SecurityHubAwsApiGatewayRestApiDetails(BaseModel):
    Id: StrictStr | None = None
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    CreatedDate: StrictStr | None = None
    Version: StrictStr | None = None
    BinaryMediaTypes: list[StrictStr] | None = None
    MinimumCompressionSize: StrictInt | None = None
    ApiKeySource: StrictStr | None = None
    EndpointConfiguration: SecurityHubAwsApiGatewayEndpointConfiguration | None = None
