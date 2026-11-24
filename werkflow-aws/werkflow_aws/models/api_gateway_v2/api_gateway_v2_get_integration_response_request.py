from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayV2GetIntegrationResponseRequest(BaseModel):
    ApiId: StrictStr
    IntegrationId: StrictStr
    IntegrationResponseId: StrictStr
