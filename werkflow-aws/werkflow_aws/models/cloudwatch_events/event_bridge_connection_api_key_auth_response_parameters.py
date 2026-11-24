from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EventBridgeConnectionApiKeyAuthResponseParameters(BaseModel):
    ApiKeyName: StrictStr | None = None
