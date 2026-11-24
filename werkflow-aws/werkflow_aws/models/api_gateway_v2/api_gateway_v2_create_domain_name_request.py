from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .api_gateway_v2_domain_name_configuration import APIGatewayV2DomainNameConfiguration
from .api_gateway_v2_mutual_tls_authentication_input import APIGatewayV2MutualTlsAuthenticationInput


class APIGatewayV2CreateDomainNameRequest(BaseModel):
    DomainName: StrictStr
    DomainNameConfigurations: list[APIGatewayV2DomainNameConfiguration] | None = None
    MutualTlsAuthentication: APIGatewayV2MutualTlsAuthenticationInput | None = None
    RoutingMode: Literal['API_MAPPING_ONLY', 'ROUTING_RULE_ONLY', 'ROUTING_RULE_THEN_API_MAPPING'] | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
