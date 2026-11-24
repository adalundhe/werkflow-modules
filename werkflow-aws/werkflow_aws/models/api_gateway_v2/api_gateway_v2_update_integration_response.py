from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .api_gateway_v2_tls_config import APIGatewayV2TlsConfig


class APIGatewayV2UpdateIntegrationResponse(BaseModel):
    ApiGatewayManaged: StrictBool | None = None
    ConnectionId: StrictStr | None = None
    ConnectionType: StrictStr | None = None
    ContentHandlingStrategy: StrictStr | None = None
    CredentialsArn: StrictStr | None = None
    Description: StrictStr | None = None
    IntegrationId: StrictStr | None = None
    IntegrationMethod: StrictStr | None = None
    IntegrationResponseSelectionExpression: StrictStr | None = None
    IntegrationSubtype: StrictStr | None = None
    IntegrationType: StrictStr | None = None
    IntegrationUri: StrictStr | None = None
    PassthroughBehavior: StrictStr | None = None
    PayloadFormatVersion: StrictStr | None = None
    RequestParameters: dict[StrictStr, StrictStr] | None = None
    RequestTemplates: dict[StrictStr, StrictStr] | None = None
    ResponseParameters: dict[StrictStr, dict[StrictStr, StrictStr]] | None = None
    TemplateSelectionExpression: StrictStr | None = None
    TimeoutInMillis: StrictInt | None = None
    TlsConfig: APIGatewayV2TlsConfig | None = None
    ResponseMetadata: dict[str, Any] | None = None
