from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .api_gateway_v2_domain_name_configuration import APIGatewayV2DomainNameConfiguration
from .api_gateway_v2_mutual_tls_authentication import APIGatewayV2MutualTlsAuthentication


class APIGatewayV2CreateDomainNameResponse(BaseModel):
    ApiMappingSelectionExpression: StrictStr | None = None
    DomainName: StrictStr | None = None
    DomainNameArn: StrictStr | None = None
    DomainNameConfigurations: list[APIGatewayV2DomainNameConfiguration] | None = None
    MutualTlsAuthentication: APIGatewayV2MutualTlsAuthentication | None = None
    RoutingMode: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
