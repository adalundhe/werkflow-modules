from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .api_gateway_v2_tls_config_input import APIGatewayV2TlsConfigInput


class APIGatewayV2UpdateIntegrationRequest(BaseModel):
    ApiId: StrictStr
    IntegrationId: StrictStr
    ConnectionId: StrictStr | None = None
    ConnectionType: Literal['INTERNET', 'VPC_LINK'] | None = None
    ContentHandlingStrategy: Literal['CONVERT_TO_BINARY', 'CONVERT_TO_TEXT'] | None = None
    CredentialsArn: StrictStr | None = None
    Description: StrictStr | None = None
    IntegrationMethod: StrictStr | None = None
    IntegrationSubtype: StrictStr | None = None
    IntegrationType: Literal['AWS', 'HTTP', 'MOCK', 'HTTP_PROXY', 'AWS_PROXY'] | None = None
    IntegrationUri: StrictStr | None = None
    PassthroughBehavior: Literal['WHEN_NO_MATCH', 'NEVER', 'WHEN_NO_TEMPLATES'] | None = None
    PayloadFormatVersion: StrictStr | None = None
    RequestParameters: dict[StrictStr, StrictStr] | None = None
    RequestTemplates: dict[StrictStr, StrictStr] | None = None
    ResponseParameters: dict[StrictStr, dict[StrictStr, StrictStr]] | None = None
    TemplateSelectionExpression: StrictStr | None = None
    TimeoutInMillis: StrictInt | None = None
    TlsConfig: APIGatewayV2TlsConfigInput | None = None
