from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayV2GetIntegrationRequest(BaseModel):
    ApiId: StrictStr
    IntegrationId: StrictStr
