from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class CognitoSyncGetCognitoEventsResponse(BaseModel):
    Events: dict[StrictStr, StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
