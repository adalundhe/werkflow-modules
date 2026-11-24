from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EventBridgeCreateConnectionApiKeyAuthRequestParameters(BaseModel):
    ApiKeyName: StrictStr
    ApiKeyValue: StrictStr
