from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .api_gateway_tls_config import APIGatewayTlsConfig


class APIGatewayPutIntegrationRequest(BaseModel):
    restApiId: StrictStr
    resourceId: StrictStr
    httpMethod: StrictStr
    type: Literal['HTTP', 'AWS', 'MOCK', 'HTTP_PROXY', 'AWS_PROXY']
    integrationHttpMethod: StrictStr | None = None
    uri: StrictStr | None = None
    connectionType: Literal['INTERNET', 'VPC_LINK'] | None = None
    connectionId: StrictStr | None = None
    credentials: StrictStr | None = None
    requestParameters: dict[StrictStr, StrictStr] | None = None
    requestTemplates: dict[StrictStr, StrictStr] | None = None
    passthroughBehavior: StrictStr | None = None
    cacheNamespace: StrictStr | None = None
    cacheKeyParameters: list[StrictStr] | None = None
    contentHandling: Literal['CONVERT_TO_BINARY', 'CONVERT_TO_TEXT'] | None = None
    timeoutInMillis: StrictInt | None = None
    tlsConfig: APIGatewayTlsConfig | None = None
    responseTransferMode: Literal['BUFFERED', 'STREAM'] | None = None
    integrationTarget: StrictStr | None = None
