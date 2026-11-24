from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .api_gateway_integration_response import APIGatewayIntegrationResponse
from .api_gateway_tls_config import APIGatewayTlsConfig


class APIGatewayIntegration(BaseModel):
    type: StrictStr | None = None
    httpMethod: StrictStr | None = None
    uri: StrictStr | None = None
    connectionType: StrictStr | None = None
    connectionId: StrictStr | None = None
    credentials: StrictStr | None = None
    requestParameters: dict[StrictStr, StrictStr] | None = None
    requestTemplates: dict[StrictStr, StrictStr] | None = None
    passthroughBehavior: StrictStr | None = None
    contentHandling: StrictStr | None = None
    timeoutInMillis: StrictInt | None = None
    cacheNamespace: StrictStr | None = None
    cacheKeyParameters: list[StrictStr] | None = None
    integrationResponses: dict[StrictStr, APIGatewayIntegrationResponse] | None = None
    tlsConfig: APIGatewayTlsConfig | None = None
    responseTransferMode: StrictStr | None = None
    integrationTarget: StrictStr | None = None
