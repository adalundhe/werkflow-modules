from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayDeleteApiKeyRequest(BaseModel):
    apiKey: StrictStr
