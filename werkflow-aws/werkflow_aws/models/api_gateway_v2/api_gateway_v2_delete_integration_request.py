from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayV2DeleteIntegrationRequest(BaseModel):
    ApiId: StrictStr
    IntegrationId: StrictStr
