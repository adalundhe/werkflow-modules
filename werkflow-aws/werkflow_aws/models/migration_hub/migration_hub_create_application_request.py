from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .migration_hub_api_gateway_proxy_input import MigrationHubApiGatewayProxyInput


class MigrationHubCreateApplicationRequest(BaseModel):
    EnvironmentIdentifier: StrictStr
    Name: StrictStr
    ProxyType: Literal['API_GATEWAY']
    VpcId: StrictStr
    ApiGatewayProxy: MigrationHubApiGatewayProxyInput | None = None
    ClientToken: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
