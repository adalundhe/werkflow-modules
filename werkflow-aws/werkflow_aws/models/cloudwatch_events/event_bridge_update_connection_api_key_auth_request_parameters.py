from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EventBridgeUpdateConnectionApiKeyAuthRequestParameters(BaseModel):
    ApiKeyName: StrictStr | None = None
    ApiKeyValue: StrictStr | None = None
