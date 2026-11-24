from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class APIGatewayGetApiKeyRequest(BaseModel):
    apiKey: StrictStr
    includeValue: StrictBool | None = None
