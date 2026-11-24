from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class APIGatewayPutGatewayResponseRequest(BaseModel):
    restApiId: StrictStr
    responseType: Literal['DEFAULT_4XX', 'DEFAULT_5XX', 'RESOURCE_NOT_FOUND', 'UNAUTHORIZED', 'INVALID_API_KEY', 'ACCESS_DENIED', 'AUTHORIZER_FAILURE', 'AUTHORIZER_CONFIGURATION_ERROR', 'INVALID_SIGNATURE', 'EXPIRED_TOKEN', 'MISSING_AUTHENTICATION_TOKEN', 'INTEGRATION_FAILURE', 'INTEGRATION_TIMEOUT', 'API_CONFIGURATION_ERROR', 'UNSUPPORTED_MEDIA_TYPE', 'BAD_REQUEST_PARAMETERS', 'BAD_REQUEST_BODY', 'REQUEST_TOO_LARGE', 'THROTTLED', 'QUOTA_EXCEEDED', 'WAF_FILTERED']
    statusCode: StrictStr | None = None
    responseParameters: dict[StrictStr, StrictStr] | None = None
    responseTemplates: dict[StrictStr, StrictStr] | None = None
