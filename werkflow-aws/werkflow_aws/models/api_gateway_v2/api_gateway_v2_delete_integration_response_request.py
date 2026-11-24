from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayV2DeleteIntegrationResponseRequest(BaseModel):
    ApiId: StrictStr
    IntegrationId: StrictStr
    IntegrationResponseId: StrictStr
